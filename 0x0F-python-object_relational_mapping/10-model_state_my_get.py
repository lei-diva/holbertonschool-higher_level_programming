#!/usr/bin/python3

if __name__ == "__main__":
    from model_state import Base, State
    import sys
    from sys import argv
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2],
                                   argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    flag = 0

    for state in session.query(State).order_by(State.id).all():
        if argv[4] == state.name:
            print(state.id)
            session.close()
            sys.exit()



    print("Not found")


    session.close()