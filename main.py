from in_memory_db import InMemoryDBImpl

def main():
    inmemoryDB = InMemoryDBImpl()

    print("get(A):", inmemoryDB.get("A"))  # None

    try:
        inmemoryDB.put("A", 5)
    except Exception as e:
        print("Expected exception:", str(e))

    inmemoryDB.begin_transaction()
    inmemoryDB.put("A", 5)

    print("get(A):", inmemoryDB.get("A"))  # None

    inmemoryDB.put("A", 6)
    inmemoryDB.commit()

    print("get(A):", inmemoryDB.get("A"))  # 6

    try:
        inmemoryDB.commit()
    except Exception as e:
        print("Expected exception:", str(e))

    try:
        inmemoryDB.rollback()
    except Exception as e:
        print("Expected exception:", str(e))

    print("get(B):", inmemoryDB.get("B"))  # None


    inmemoryDB.begin_transaction()
    inmemoryDB.put("B", 10)
    inmemoryDB.rollback()

    print("get(B):", inmemoryDB.get("B"))  # None

if __name__ == "__main__":
    main()
