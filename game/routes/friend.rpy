label friend_route_start:
    scene bg university_common
    show friend fullbody_default at fullbody_fit
    with fade

    narrator "【하린 루트】"
    friend "요즘 너 나랑 자주 다니네."
    p "싫어?"
    show friend fullbody_surprise at fullbody_fit
    friend "아니. 그래서 물어본 거야."

    menu:
        "친구 이상으로 보고 있다고 말한다.":
            $ friend_courage += 1
            $ friend_affection += 10
            p "난 너 그냥 친구로만 보는 거 아니야."
            show friend fullbody_flustered at fullbody_fit
            friend "...그걸 이제 말하냐."

        "괜히 분위기를 망치기 싫어 농담으로 넘긴다.":
            p "복학생 챙겨주는 착한 친구니까 붙어 다니는 거지."
            show friend fullbody_sadness at fullbody_fit
            friend "그래. 친구니까."

    show friend fullbody_jealousy at fullbody_fit
    narrator "며칠 뒤 하린은 다른 학교 선배에게 연락이 왔다고 말했다."

    menu:
        "오늘은 나와 있어 달라고 말한다.":
            $ friend_courage += 1
            p "오늘은 그 사람 말고 나랑 있어."
            show friend fullbody_flustered at fullbody_fit
            friend "그거... 무슨 뜻인지 알고 하는 말이지?"

        "선택은 하린 몫이라며 보내준다.":
            p "네가 만나고 싶으면 만나."
            show friend fullbody_sadness at fullbody_fit
            friend "응. 그럼 다녀올게."

    if friend_courage >= 4:
        call screen chapter_transition("하린 해피 엔딩", "친구 다음의 이름")
        jump friend_happy
    else:
        call screen chapter_transition("하린 배드 엔딩", "보내지 못한 메시지")
        jump friend_bad

label friend_happy:
    scene bg university_common
    show friend fullbody_default at fullbody_fit
    narrator "축제가 끝난 늦은 밤."
    show friend fullbody_joy at fullbody_fit
    friend "군대 가기 전에도 이 말 기다렸는데."
    p "그때는 몰랐어."
    show friend fullbody_flustered at fullbody_fit
    friend "그럼 지금부터 갚아. 오래 걸렸으니까."
    $ ending_seen = "friend_happy"
    centered "HARIN HAPPY END\n친구 다음의 이름"
    return

label friend_bad:
    scene black
    narrator "새벽 1시 47분."
    narrator "하린에게서 메시지가 하나 도착했다."
    friend "나 오늘 집 안 들어갈 듯. 내일 연락할게."
    narrator "함께 온 사진 구석에는 익숙하지 않은 숙박업소 간판이 찍혀 있었다."
    p "누구랑 있는데?"
    narrator "나는 문장을 지웠다."
    p "집 들어가."
    narrator "그것도 지웠다."
    narrator "결국 아무것도 보내지 못했다."
    $ ending_seen = "friend_bad"
    centered "HARIN BAD END\n보내지 못한 메시지"
    return
