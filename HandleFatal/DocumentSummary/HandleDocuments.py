from DBconn.db_connection import conn


def insert_documents_summary(incident_json):
    """
    inserts the documents from the fatality database into the database. This includes images from SAR and other articles etc
    """

    core_url = "https://incidents.avalanche.ca"

    cursor = conn.cursor()

    documents_json = incident_json['documents']

    unique_id = incident_json['id']

    for document in documents_json:
        insert_query = """
        INSERT INTO documents (date, doc_desc, source,  link, id)
        VALUES (%s, %s, %s, %s, %s)
        """
# control for when the date is in a list for some reason
        if (type(document.get('date')) == list):
            document['date'] = document['date'][0]

        data = (
            document.get('date'),
            document.get('title'),
            document.get('source'),
            core_url + document.get('url'),
            unique_id
        )

        try:
            cursor.execute(insert_query, data)
            conn.commit()
            print(f"Record {unique_id} inserted     successfully")
        except Exception as e:
            print(f"Error for {unique_id}: {e}")
