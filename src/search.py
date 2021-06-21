from elasticsearch_dsl import Search, Q
from elasticsearch_dsl.connections import connections


if __name__ == "__main__":

    with connections.create_connection(hosts="localhost:9200"):

        search = Search(index="basic-info-index")
        # search = search.query(
        #     Q(
        #         "nested", 
        #         path="keys", 
        #         query=Q(
        #             "match", 
        #             keys__name="bbb",
        #         )
        #     )
        # )
        response = search.params(raise_on_error=False, size=10000).scan() 

        for row in response:
            print("id:", row.id)
            print("text:", row.text)

            keys = row.keys
            for key in keys:
                print("\tkey name:", key.name)
                positions = key.positions
                for position in positions:
                    print("\t\tkey position:", position.start, position.end)