label older_route_start:
    scene black
    show older_sheet at sheet_fit
    with fade

    narrator "【서윤 루트】"
    older "저번에는... 죄송했어요."
    p "교수님이 찾는다고 한 거요?"
    older "네. 그때는 그냥... 도망가고 싶어서."

    menu:
        "왜 도망갔는지 말할 때까지 기다린다.":
            $ older_trust += 1
            $ older_affection += 10
            p "말하기 싫으면 지금 안 해도 돼요."
            older "그렇게 말하면 더 미안해지는데..."

        "내가 싫어서 그런 건지 확답을 요구한다.":
            p "저 싫어서 그런 거였어요?"
            older "아니에요. 그 반대라서... 더 문제였어요."

    narrator "며칠 뒤, 서윤은 계약이 끝나면 학교를 떠날 생각이라고 말했다."

    menu:
        "떠나기 전에 관계를 분명하게 하고 싶다고 말한다.":
            $ older_trust += 1
            p "조교님이 떠나는 것과 제가 좋아하는 건 별개잖아요."
            older "...그런 말을 그렇게 바로 해도 되는 거예요?"

        "부담스러울까 봐 아무 말도 하지 않는다.":
            p "그렇군요."
            older "네."

    if older_trust >= 4:
        jump older_happy
    else:
        jump older_bad

label older_happy:
    scene black
    show older_sheet at sheet_fit
    narrator "학교 근처 편의점 앞. 늦은 저녁."
    older "저 오늘은 안 도망갔어요."
    p "알아요."
    older "앞으로도... 연습해 볼게요."
    p "천천히 해요. 같이."
    $ ending_seen = "older_happy"
    centered "SEOYUN HAPPY END\n도망가지 않는 연습"
    return

label older_bad:
    scene black
    narrator "며칠 뒤부터 서윤은 학과사무실에 나오지 않았다."
    narrator "메신저는 읽히지 않았고 전화도 연결되지 않았다."
    narrator "한참 뒤에야 그녀가 조교 업무를 정리하고 학교를 떠났다는 말을 들었다."
    p "...마지막 말조차 못 했네."
    $ ending_seen = "older_bad"
    centered "SEOYUN BAD END\n잠수"
    return
