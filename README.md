# django

### 함수 기반 뷰(FBV)(일회성)
장점 
• 구현이 간편함
• 읽기 쉬우며 직관적인 코드
• 데코레이터의 간단한 사용법
단점
• 코드 확장과 재사용이 어려움
• 조건부 분기를 통한 HTTP 메서드 처리

### 클래스 기반 뷰(CBV)
장점 
• 코드 확장과 재사용 용이
• 다중 상속, Mixin 가능
• 내장 Class Based View 사용
단점
• 읽기 어려우며 복잡도가 높음
• 데코레이터 사용 시 함수를 재정의 해야
함

### Template은 서버에서 실행

### Template 태그
* block: 자식 템플릿으로 재정의할 수 있는 블록 {% block name %} {% endblock %}

* extends: 부모 템플릿을 확장, 상속 {% extends 'template_name' %}

* include:  템플릿을 로드하고 현재 Context로 렌더링, 템플릿 포함 {% include template_name %}

###  Template 필터
* date: 주어진 형식에 따라 날짜 형식을 지정합니다. {{ value|date:"D d M Y" }}
* center 주어진 너비의 필드에서 값을 가운데에 맞춥니다. "{{ value|center:"15" }} (format 함수랑 비슷)
