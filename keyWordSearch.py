# 키워드를 입력하면 해당 텍스트 파일에서 입력한 단어가 몇번 등장하는지 알려주는 프로그램

print("**************************************************")
print("검색할 키워드를 입력하세요.")
keyWord = input(">> ")

# 파일 오픈
f = open("speach.txt", "r")

# 문자열 다 긁어오기
all_sentence = f.read()

# 제거할 문자들을 지정
remove_chars = ",.!?*" 

# 'str.maketrans()'를 사용하여 빈 변환 테이블을 생성
trans_table = str.maketrans("", "", remove_chars)

# 'str.translate()'를 사용하여 입력 문자열에서 지정한 문자들을 제거.
cleaned_string = all_sentence.translate(trans_table)

# 연설문 내 단어들을 띄어쓰기 단위로 잘러서 리스트의 요소로 변환
wordList = cleaned_string.split()

count = 0
for word in wordList:
    if keyWord in word:
        count += 1
print("해당 연설문 안에서 ")
print(f"\'{keyWord}\'라는 단어는 총 {count}번 등장합니다.")
print("**************************************************")


# 파일 close
f.close()