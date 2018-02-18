import discord
import random
import asyncio
import pickle
import os

Client = discord.Client()

@Client.event
async def on_ready():
    print("푸딩봇 온라인!")
    print("pudding-bot is now online!")

@Client.event
async def on_message(message):
    if message.content.startswith('푸딩아 안녕'):
        hello = random.choice(['ㅎㅇㅎㅇ!','안뇽!','하이하이!','하이!','ㅎㅇ!','ㅇㅇ','나도 안녕','안녕!','헬로우~!','나도 안뇽!!','반갑다!','헤헿'])
        await Client.send_message(message.channel, hello)
    elif message.content.startswith('푸딩아 뭐해'):
        what = random.choice(['난 유튜브 보는중이지!','마인크래프트 하이픽셀에서 스카이워즈 돌리고 있었는데 핵이 막 욕해서 마음 아팠음..','여친이랑 카톡중! (가상 여친..)','너랑 채팅중이지 근데 은근 재밌음','핸드폰 게임하는중 요즘 프파 재밌드라..','배그 하는중.. 나도 핵한번 써볼까?','나도 안녕','안녕!','헬로우~!','마인크래프트 1.12 버전에서 신나게 야생하고 있다 지금 다이아몬드 7개임','zzZ','(지금 학원에서 몰폰 하는 중이야 쉿!','학교에서 핸드폰으로 음악듣는중!','교과서 에다가 열심히 낙서중.. 곧 있으면 졸업이라니! 흐규흐규 ㅠㅠ','디스코드에서 뭐 할거 없나 보는중임','푸딩봇 개발 버전 개발중!','코딩중이니까 건들지마.','오랜만에 파이썬 사용하니까 익숙치가 않네..','게임중..','침대에 엎드려서 핸드폰으로 영상 보는중','아는 여자애랑 톡중..','친구 "젤리"랑 열심히 노는중','신나게 파티중'])
        await Client.send_message(message.channel, what)
    elif message.content.startswith('푸딩아 버전'):
        await Client.send_message(message.channel, '푸딩봇의 버전: \n**Pudding - Creating Version**')
    elif message.content.startswith('ㅗ'):
        user = message.author.id
        await Client.send_message(message.channel, "<@%s> 야 이쁜말좀 쓰자^^" % (user))
    elif message.content.startswith('씨발'):
        user = message.author.id
        await Client.send_message(message.channel, "<@%s> 바르고 고운말좀 씁시다 우리 예?" % (user))
    elif message.content.startswith('시발'):
        user = message.author.id
        await Client.send_message(message.channel, "<@%s> 바르고 고운말좀 씁시다 우리 예?" % (user))
    elif message.content.startswith('병신'):
        user = message.author.id
        await Client.send_message(message.channel, "<@%s> 바르고 고운말좀 씁시다 우리 예?" % (user))
    elif message.content.startswith('븅진'):
        user = message.author.id
        await Client.send_message(message.channel, "<@%s> 바르고 고운말좀 씁시다 우리 예?" % (user))
    elif message.content.startswith('븅신'):
        user = message.author.id
        await Client.send_message(message.channel, "<@%s> 바르고 고운말좀 씁시다 우리 예?" % (user))
    elif message.content.startswith('애미'):
        user = message.author.id
        await Client.send_message(message.channel, "<@%s> 바르고 고운말좀 씁시다 우리 예?" % (user))
    elif message.content.startswith('뒤질레'):
        user = message.author.id
        await Client.send_message(message.channel, "<@%s> 바르고 고운말좀 씁시다 우리 예?" % (user))
    elif message.content.startswith('병진'):
        user = message.author.id
        await Client.send_message(message.channel, "<@%s> 바르고 고운말좀 씁시다 우리 예?" % (user))
    elif message.content.startswith('쉬발'):
        user = message.author.id
        await Client.send_message(message.channel, "<@%s> 바르고 고운말좀 씁시다 우리 예?" % (user))
    elif message.content.startswith('찌발'):
        user = message.author.id
        await Client.send_message(message.channel, "<@%s> 바르고 고운말좀 씁시다 우리 예?" % (user))
    elif message.content.startswith('새끼'):
        user = message.author.id
        await Client.send_message(message.channel, "<@%s> 바르고 고운말좀 씁시다 우리 예?" % (user))
    elif message.content.startswith('섹스'):
        user = message.author.id
        await Client.send_message(message.channel, "<@%s>, 변태세요?" % (user))
    elif message.content.startswith('부랄'):
        user = message.author.id
        await Client.send_message(message.channel, "<@%s>, 변태세요?" % (user))
    elif message.content.startswith('지랄'):
        user = message.author.id
        await Client.send_message(message.channel, "<@%s> 바르고 고운말좀 씁시다 우리 예?" % (user))
    elif message.content.startswith('느금마'):
        user = message.author.id
        await Client.send_message(message.channel, "<@%s> 바르고 고운말좀 씁시다 우리 예?" % (user))
    elif message.content.startswith('엿먹어'):
        user = message.author.id
        await Client.send_message(message.channel, "<@%s> 바르고 고운말좀 씁시다 우리 예?" % (user))
    elif message.content.startswith('쉬벌'):
        user = message.author.id
        await Client.send_message(message.channel, "<@%s> 바르고 고운말좀 씁시다 우리 예?" % (user))
    elif message.content.startswith('시벌'):
        user = message.author.id
        await Client.send_message(message.channel, "<@%s> 바르고 고운말좀 씁시다 우리 예?" % (user))
    elif message.content.startswith('씨벌'):
        user = message.author.id
        await Client.send_message(message.channel, "<@%s> 바르고 고운말좀 씁시다 우리 예?" % (user))
    elif message.content.startswith('쒸벌'):
        user = message.author.id
        await Client.send_message(message.channel, "<@%s> 바르고 고운말좀 씁시다 우리 예?" % (user))
    elif message.content.startswith('쒸발'):
        user = message.author.id
        await Client.send_message(message.channel, "<@%s> 바르고 고운말좀 씁시다 우리 예?" % (user))
    elif message.content.startswith('C발'):
        user = message.author.id
        await Client.send_message(message.channel, "<@%s> 바르고 고운말좀 씁시다 우리 예?" % (user))
    elif message.content.startswith('시.발'):
        user = message.author.id
        await Client.send_message(message.channel, "<@%s> 바르고 고운말좀 씁시다 우리 예?" % (user))
    elif message.content.startswith('ㅗ.'):
        user = message.author.id
        await Client.send_message(message.channel, "<@%s> 바르고 고운말좀 씁시다 우리 예?" % (user))
    elif message.content.startswith('시바알'):
        user = message.author.id
        await Client.send_message(message.channel, "<@%s> 바르고 고운말좀 씁시다 우리 예?" % (user))
    elif message.content.startswith('새끼'):
        user = message.author.id
        await Client.send_message(message.channel, "<@%s> 바르고 고운말좀 씁시다 우리 예?" % (user))
    elif message.content.startswith('푸딩아 놀아줘'):
        user =  message.author.id
        ms = "<@%s>TV 영상 보는중임 건들지 마셈" % user
        plz = random.choice(["시러 귀차늠","귀차니즘..","피곤해","너 혼자 놀아 친구 많잖아(찐1따 라면 ㅈㅅ..)","가서 게임이나해 너 게임좋아 하잖아","내가 종이냐? 니가 시키는 대로 다하게..","응 안놀아~","딴데가서 놀아 이미 노는중임.","이미 현솔이랑 노는중",ms,"나가서 놀아 밖에 친구들 많지 않음?","으어.. 피곤","여유롭게 과자먹으며 내일에 대한 나를 고민중이니까 건들지 말자^^","공부중이니까 다른 애랑 노라 예를 들어 '젤리봇'이라 던지 (없으면 ㅈㅅ)","누가 놀기 싫테니 난 지금 미래의 나를 위해 공부중이라구","노래좀 듣자 이노래 좋다. 노래이름: '현솔의 소풍'","너는 나밖에 놀애가 없음?","가서 코딩이나해 나도 지금 젤리봇 업데이트 시키는 중임.","현솔 아이카#2377 한테 놀아 달라해 재밌게 놀아줄거임(아마도..)","시른데요 저 뚱인데요?(ㄵ이라 ㅈㅅ)","..ㅉ"])
        await Client.send_message(message.channel, plz)
    elif message.content.startswith('푸딩아 찐따'):
        jinda = random.choice(["디진다 진짜", "하..","너도 ㅋ",'YOU TO'])
        await Client.send_message(message.channel, jinda)
    elif message.content.startswith('ㅇㅅㅇ'):
        await Client.send_message(message.channel, "느닛!")
    elif message.content.startswith('코와이네'):
        jp_a = random.choice(["무섭네!",'??',"일본인 이세요?","일본어?","일본어 하면 일본 일본하면 스시지(냠냠)","어메 무서워라~","난 카와이네로 하겠다!"])
        await Client.send_message(message.channel, jp_a)
    elif message.content.startswith('고사리네'):
        await Client.send_message(message.channel, "정신좀 차리세요, 고사리는 식물 이름이거든요?")
    elif message.content.startswith('푸딩아 젤리'):
        jc = random.choice(['젤리먹는 거 아님?','젤리님은 인성이 별로에요','좋지 않게 생각해요','원래 제가 먼저 업데이트 되어야 하는데 젤리봇이 먼저 업데이트 됬어요 기분 나쁩니다. 상당히','츠키요노인 이유를 모르겠어요','젤리야 놀자','콤보 뜨자','같이 노실?','젤리님 불러줘? 하긴 찐11따니깐ㅎㅎ','젤리야 뭐하니! 공부해야지!!','젤리님 열심히 공부중일거에요.. 미래를 위해! (공부 싫어해서 안할 수도 있음)','젤리는 그저 마인크래프트 PVP를 못하는 한 플레이어일 뿐이죠 젤리는 먹어야 제맛','여러분 젤리가 뭔지 아십니까? 음식입니다!','젤리님 화나면 무서움 ㄷㄷ'])
        await Client.send_message(message.channel, jc)
    elif message.content.startswith('ㅎㅎ'):
        await Client.send_message(message.channel, "헤헿^^")
    elif message.content.startswith('배고파'):
        jp_a = random.choice(["가서 밥먹으셈",'??',"마침나도 밥먹고 었는데 같이 먹으실?","밥달라고 해","집에서 꺼내먹어","나도 배고픔요","쯧쯧","거.지세요?","뭔가 안쓰러움","공감되는 말","ㅇㅈ","ㅆㅇㅈ"])
        await Client.send_message(message.channel, jp_a)
    elif message.content.startswith('푸딩아 말해'):
        args = message.content.split(" ")[2:]
        if ( args == "" ):
            await Client.send_message(message.channel, "사용법: 푸딩아 말해 [할말] ㅇㅋ?")
        else:
            await Client.send_message(message.channel, args)
        

Client.run(token)
