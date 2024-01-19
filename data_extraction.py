# data_extraction.py

from db_connection import create_connection

def extract_data():
    # 데이터베이스 연결 생성
    connection = create_connection()

    # 커서 생성
    with connection.cursor() as cursor:
        # SQL 쿼리 작성
        query = "SELECT * FROM your_table"  # your_table 부분을 실제 테이블 이름으로 변경해야 합니다.

        # SQL 쿼리 실행
        cursor.execute(query)

        # 쿼리 결과 가져오기
        result = cursor.fetchall()

    # 데이터베이스 연결 종료
    connection.close()

    return result
