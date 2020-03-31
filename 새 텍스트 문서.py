from typing import Any, Union

import discord
n = 0

client = discord.Client()
@client.event
async def on_ready():
    print(client.user.id)
    print("reday")
    game = discord.Game("!도움말을 입력해보세요")
    await client.change_presence(status=discord.Status.online, activity=game)
@client.event
async def on_message(message):
    if message.content == "!드라마":
        embed = discord.Embed(title="2분기애니정리", description="드라마")
        embed.add_field(name="코미디, 드라마", value="예스터데이를 노래하며", inline=False)
        embed.add_field(name="마법, 코미디, 드라마", value="뮤클 드리미", inline=False)
        embed.add_field(name="아이돌, 코미디, 드라마", value="아이돌리쉬 세븐 second BEAT!", inline=False)
        embed.add_field(name="배틀, 드라마, 스포츠", value="BNA", inline=False)
        embed.add_field(name="드라마, 추리", value="부호형사 balance:UNLIMITED", inline=False)
        embed.add_field(name="드라마, 능력", value="문호와 알케미스 트 심판의 톱니바퀴", inline=False)
        embed.add_field(name="직업 드라마", value="파도여 들어다오", inline=False)
        embed.add_field(name="드라마, 학원, 스포츠", value="메이저 세컨드", inline=False)
        embed.add_field(name="드라마", value="아르테", inline=False)
        await message.channel.send(embed=embed)
    if message.content == "!이세계":
        embed = discord.Embed(title="2분기애니정리", description="이세계")
        embed.add_field(name="판타지, 이세계, 코미디", value="여성향 게임의 파멸 플래그 밖에 없는 악역 영애로 환생해버렸다", inline=False)
        embed.add_field(name="판타지, 이세계, 코미디, 일상", value="책벌레의 하극상 사서가 되기 위해서라면 뭐든지 할수있어", inline=False)
        embed.add_field(name="판타지, 이세계, 코미디, 일상", value="사장님, 배틀 시간입니다!", inline=False)
        embed.add_field(name="판타지, 이세계", value="팔남이라니 그건 아니지!", inline=False)
        await message.channel.send(embed=embed)
    if message.content == "!도움말":
        embed = discord.Embed(title="도움말", description="명령어를 참고해주세요")
        embed.add_field(name="애니", value="!액션  ,  !이세계   ,  !학원     ,     !드라마       , !판타지       , !기타")
        await message.channel.send(embed=embed)
    if message.content == "!2분기애니":
        await message.channel.send("어떤 장르?")
    if message.content == "!액션":
        embed = discord.Embed(title="2분기애니정리", description="액션")
        embed.add_field(name="SF 게임 액션 먼치킨", value="소드 아트 온라인 앨리시제이션 war of underworld", inline=False)
        embed.add_field(name="판타지, 액션, 하렘", value="계 츠구모모", inline=False)
        embed.add_field(name="액션, 판타지", value="하얀고양이 프로젝트 제로 크로니클", inline=False)
        embed.add_field(name="액션, 시대", value="신 사쿠라 대전 the animation", inline=False)
        await message.channel.send(embed=embed)
    if message.content == "!학원":
        await message.channel.send(embed=embed)
        embed = discord.Embed(title="2분기애니정리", description="학원")
        embed.add_field(name="학원, 로맨스, 드라마", value="후르츠 바스켓 2시즌", inline= False)
        embed.add_field(name="방과후 제방 일지", value="학원, 일상, 부활동", inline=False)
        embed.add_field(name="부활동, 하렘, 학원", value="역시 내 청춘 러브코메디는 잘못됐다 완", inline=False)
        embed.add_field(name="학원, 요리, 배틀", value="식극의 소마 다섯 번째 접시", inline=False)
        embed.add_field(name="드라마, 학원, 스포츠", value="메이저 세컨드", inline=False)
        embed.add_field(name="학원, 코미디, 일상", value="카구야 님은 고백받고 싶어? 천재들의 연애 두뇌전", inline=False)
    if message.content == "!판타지":
        embed = discord.Embed(title="2분기애니정리", description="판타지")
        embed.add_field(name="판타지, 이세계, 코미디", value="여성향 게임의 파멸 플래그 밖에 없는 악역 영애로 환생해버렸다", inline=False)
        embed.add_field(name="판타지, 이세계, 코미디, 일상", value="책벌레의 하극상 사서가 되기 위해서라면 뭐든지 할수있어", inline=False)
        embed.add_field(name="판타지, 배틀", value="글레이프니르", inline=False)
        embed.add_field(name="판타지, 이세계, 배틀", value="판타지, 이세계, 배틀", inline=False)
        embed.add_field(name="액션, 판타지", value="하얀고양이 프로젝트 제로 크로니클", inline=False)
        embed.add_field(name="일상, 판타지, 코미디", value="사신짱 드롭킥 2기", inline=False)
        embed.add_field(name="판타지", value="프린세스 커넥트! re:dive", inline=False)
        embed.add_field(name="판타지, 이세계", value="팔남이라니 그건 아니지!", inline=False)
        embed.add_field(name="판타지, 모험", value="천청난만!", inline=False)
        await message.channel.send(embed=embed)
    if message.content == "!기타":
        embed = discord.Embed(title="2분기애니정리", description="기타")
        embed.add_field(name="능력, 모험, 코미디", value="디지몬 어드벤쳐", inline=False)
        embed.add_field(name="귀신, 추리, 요괴", value="탁목조 탐정처", inline=False)
        embed.add_field(name="메카닉, 능력, 전투", value="섀도우버스", inline=False)
        embed.add_field(name="스포츠, 부활동", value="타마요미", inline=False)
        embed.add_field(name="일상, 코미디", value="카쿠시고토", inline=False)
        embed.add_field(name="일상, 부활동, 음악", value="아르고나비스", inline=False)
        embed.add_field(name="기타", value="리스너즈", inline=False)
        await message.chennel.send(embed=embed)












client.run('Njk0NTA4MDI4NzcwMzg1OTkw.XoMpMQ.DIMzLPh2aqSKw4xcKo93eqS1HiI')
