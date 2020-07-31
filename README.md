restaurant_API



## 음식점 List API

- URL

  ​	GET localhost:8000/restaurant/list/<<int:page>>

  ​	GET localhost:8000/restaurant/list



- Request

  - URL parameter

    ​	page : Integer, element가 20개인 n번째 페이지



- Process

  ​	url parameter를 통해 표현해야할 page를 전달받습니다. page가 전달되지 않은 경우 기본값 1을 갖습니다

  ​	page값을 통해 offset과 limit를 계산하여 queryset에 슬라이싱 형태로 적용합니다

  ​	이 후 평가된 쿼리셋을 순회하여 정의한 to_json 메소드를 통해 리스트 내부의 dictionary형태로 리턴합니다



## 음식점 Detail API

- URL

  ​	GET localhost:8000/restaurant/<<int:restaurant_id>>



- Request

  - URL parameter

    ​	restaurant_id : Integer, Detail info를 조회할 restaurant의 id



- Process

  ​	prefetch_related를 사용하여 menu_set을 캐시한 Restaurant 객체를 로드합니다

  ​	Restaurant객체에서 to_json 메소드를 사용하여 dictionary형태로 만들고

  ​	해당 객체에 캐시된 menu_set을 역참조 하여 관계된 menu들에 대해서 to_json 메소드를 호출하여

  ​	dictionary에 추가하여 리턴합니다

  ​	restaurant_id에 해당하는 레코드가 존재하지 않을경우 http status code 400을 리턴합니다

  

## 음식점 Create API

- URL

  ​	POST localhost:8000/restaurant



- Request

  - body

    ​	name : String , 음식점 이름

    ​    description : String, 음식점 소개

    ​    address: : String, 음식점 주소

    ​    phone_number : String, 음식점 전화번호



- Process

  ​	request body의 값을 dictionary로 로드합니다

  ​	dictionary에 API에서 요구하는 키값이 존재하지 않거나, 값이 전달되지 않았을 경우

  ​	http status code 400을 리턴합니다

  ​	로드한 dictionary를 언패킹하여 Restorant의 object매니저를 통해 create합니다

  ​	만들어진 restorant 인스턴스에서 to_json 메소드를 호출하여 결과를 리턴합니다



## 메뉴 Create API

- URL

  ​	POST localhost:8000/restaurant/menu



- Request

  - body

    ​	restaurant_id : Integer, 메뉴가 속하는 음식점 id

    ​    name : String, 메뉴의 이름

    ​    price : Integer, 메뉴의 가격



- Process

  request body의 값을 dictionary로 로드합니다

  dictionary에 API에서 요구하는 키값이 존재하지 않거나, 값이 전달되지 않았을 경우

  http status code 400을 리턴합니다

  로드한 dictionary를 언패킹하여 Restorant의 object매니저를 통해 create합니다

  restaurant_id에 해당하는 음식점이 존재하지 않을 경우 http status code 400을 리턴합니다

  