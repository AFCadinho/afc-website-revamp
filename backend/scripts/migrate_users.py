import os
import sqlalchemy as sa
import sys

from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from database.database import engine as new_engine
from database.models import User


load_dotenv()

OLD_DATABASE_URL = os.getenv("OLD_DATABASE_URL")
if not OLD_DATABASE_URL:
    raise ValueError("OLD_DATABASE_URL is not set")

old_engine = sa.create_engine(OLD_DATABASE_URL, pool_pre_ping=True)

OldSession = sessionmaker(bind=old_engine)
NewSession = sessionmaker(bind=new_engine, autoflush=False, expire_on_commit=False)


def migrate_users() -> None:
    query = sa.text("""
        SELECT
            name,
            email,
            password,
            is_email_confirmed,
            is_admin,
            is_banned,
            created_at
        FROM users
        WHERE email IS NOT NULL
        ORDER BY id
    """)

    with OldSession() as old_session, NewSession.begin() as new_session:
        old_users = old_session.execute(query).mappings().all()

        existing_emails = set(new_session.scalars(sa.select(User.email)).all())
        existing_names = set(new_session.scalars(sa.select(User.name)).all())

        migrated = 0
        skipped = 0

        for old_user in old_users:
            if (
                old_user["email"] in existing_emails
                or old_user["name"] in existing_names
            ):
                skipped += 1
                continue

            new_user = User(
                name=old_user["name"],
                email=old_user["email"],
                password=old_user["password"],
                is_email_confirmed=bool(old_user["is_email_confirmed"]),
                is_admin=bool(old_user["is_admin"]),
                is_banned=bool(old_user["is_banned"]),
                created_at=old_user["created_at"],
            )
            new_session.add(new_user)

            existing_emails.add(old_user["email"])
            existing_names.add(old_user["name"])

            migrated += 1

        print(f"Found: {len(old_users)}")
        print(f"Migrated: {migrated}")
        print(f"Skipped: {skipped}")


if __name__ == "__main__":
    migrate_users()