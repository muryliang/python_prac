import shelve as sh

def store(db):
    person = {}
    mid = raw_input("Enter your id: ")
    person['age'] = raw_input("Age: ")
    person['name'] = raw_input("Name: ")
    db[mid] = person

def lookup(db):
    mid = raw_input("Search id: ")
    obj = raw_input("Search attr(age,name): ")
    obj = obj.strip().lower()
    print obj.capitalize() + ": " + db[mid][obj]

def getcmd():
    cmd = raw_input("which command?(? for help ")
    cmd = cmd.strip().lower()
    return cmd

def helpinfo():
    print """
    availiable options:
    store lookup help ? quit
    """

def main():
    try:
        db = sh.open("db.dat")
        while True:
            cmd = getcmd()
            if cmd == "store":
                store(db)
            elif cmd == "lookup":
                lookup(db)
            elif cmd == "help" or cmd == "?":
                helpinfo()
            elif cmd == "quit":
                return
            else:
                print "unknown option:",cmd
    finally:
        db.close()

if __name__ == "__main__":
    main()
