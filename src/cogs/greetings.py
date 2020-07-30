from discord.ext import commands
from modules import rank
from modules import Schedule
from datetime import datetime
import discord

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    month = datetime.today().month
    day = datetime.today().day
    year = datetime.today().year

    @commands.command()
    async def 안녕(self, ctx):
        await ctx.send('안녕! :wave:')

    @commands.command()
    async def 축구(self, ctx, msg=None, league='epl', year=2019):
        if(msg == None):
            embed = discord.Embed(color=0x00ff56)
            embed.set_author(name="사용법", icon_url="https://e7.pngegg.com/pngimages/121/1000/png-clipart-white-and-black-soccer-ball-with-flame-illustration-2014-fifa-world-cup-football-player-sport-fire-football-game-orange.png")
            embed.set_thumbnail(url="https://e7.pngegg.com/pngimages/121/1000/png-clipart-white-and-black-soccer-ball-with-flame-illustration-2014-fifa-world-cup-football-player-sport-fire-football-game-orange.png")
            embed.add_field(name="Rank", value="`순위 [리그명] [년도]`,`리그목록`", inline=False)
            await ctx.send(embed=embed)
        else:
            kind = msg
            print(kind, league, year)
            if (kind == '순위'):
                if(league == "프리미어리그"):
                    rank_list = rank.getRank('epl',year)
                    embed = discord.Embed(title="epl 순위", color=0x00ff56)
                    embed.set_author(name="프리미어리그 순위", icon_url="https://imgsports.pstatic.net/images/2020/pc/common/league/epl_on.png")
                    embed.set_thumbnail(url="https://t1.daumcdn.net/liveboard/sportsvod/200240cbd5354763a69e618f4034e6fe.JPG")
                elif(league == "라리가"):
                    rank_list = rank.getRank('primera',year)
                    embed = discord.Embed(title="epl 순위", color=0x00ff56)
                    embed.set_author(name="스페인 라리가 순위", icon_url="https://imgsports.pstatic.net/images/2020/pc/common/league/primera_on.png")
                    embed.set_thumbnail(url="http://photo.hankooki.com/newsphoto/v001/2020/05/30/upcoming20200530130503_P_02_C_1.jpg")
                elif(league == "분데스리가"):
                    rank_list = rank.getRank('bundesliga',year)
                    embed = discord.Embed(title="bundesliga 순위", color=0x00ff56)
                    embed.set_author(name="분데스리가 순위", icon_url="https://imgsports.pstatic.net/images/2020/pc/common/league/bundesliga_on.png")
                    embed.set_thumbnail(url="https://e7.pngegg.com/pngimages/489/415/png-clipart-bundesliga-logo-bundesliga-logo-icons-logos-emojis-football.png")
                elif(league == "세리에"):
                    rank_list = rank.getRank('seria',year)
                    embed = discord.Embed(title="seria 순위", color=0x00ff56)
                    embed.set_author(name="이탈리아 세리에 A 순위", icon_url="https://imgsports.pstatic.net/images/2020/pc/common/league/seria_on.png")
                    embed.set_thumbnail(url="https://1.bp.blogspot.com/-FuLCBTHRU-U/XWUu9FTnDtI/AAAAAAAAg0g/4Pub1pG2tNQTZlN_wNfcDYKwi0Sevgk_QCLcBGAs/s320/SerieA2019-20LogoOff.png") 
                elif(league == "프랑스리그"):
                    rank_list = rank.getRank('ligue1',year)
                    embed = discord.Embed(title="ligue1 순위", color=0x00ff56)
                    embed.set_author(name="프랑스 리그 순위", icon_url="https://imgsports.pstatic.net/images/2020/pc/common/league/ligue1_on.png")
                    embed.set_thumbnail(url="https://e7.pngegg.com/pngimages/434/605/png-clipart-2017-18-ligue-1-france-paris-saint-germain-f-c-premier-league-olympique-lyonnais-france-sport-logo.png")
                else:
                    rank_list = rank.getRank()
                    embed = discord.Embed(title="프리미어리그 순위", color=0x00ff56)
                    embed.set_author(name="프리미어리그 순위", icon_url="https://imgsports.pstatic.net/images/2020/pc/common/league/epl_on.png")
                    embed.set_thumbnail(url="https://t1.daumcdn.net/liveboard/sportsvod/200240cbd5354763a69e618f4034e6fe.JPG")
                num = 0
                print(rank_list)
                print(len(rank_list))
                team_rank_list = '!'.join(rank_list)
                while num < len(rank_list):
                    embed.add_field(name=str(num+1) + "위",value=team_rank_list.split('!')[num], inline=False)
                    num = num + 1
                await ctx.send(embed=embed)
            elif(kind == "리그목록"):
                embed = discord.Embed(color=0x00ff56)
                embed.set_author(name="리그 목록")
                embed.set_thumbnail(url="https://resources.premierleague.com/premierleague/photo/2018/11/27/3a933964-a478-4369-b9e0-44d40027205c/Rainbow-Laces-2018-Article-Lead.png")
                embed.add_field(name="순위조회", value="```프리미어리그, 라리가, 세리에, 분데스리가, 프랑스리그```", inline=False)
                embed.add_field(name="경기일정조회", value="```프리미어리그, 라리가, 세리에, 분데스리가, 프랑스리그, 챔피언스리그, 유로파리그```", inline=False)
                await ctx.send(embed=embed)
    @commands.command()
    async def 이달의경기(self, ctx, league='epl'):
        month = datetime.today().month
        embed = discord.Embed(title="일정", color=0x00ff56)
        embed2 = discord.Embed(title="일정", color=0x00ff56)
        if(league == "프리미어리그"):
                schedule_list = Schedule().month_match()
                embed = discord.Embed(title="일정", color=0x00ff56)
                embed.set_author(name="프리미어리그 일정", icon_url="https://imgsports.pstatic.net/images/2020/pc/common/league/epl_on.png")
                embed.set_thumbnail(url="https://t1.daumcdn.net/liveboard/sportsvod/200240cbd5354763a69e618f4034e6fe.JPG")
                embed2.set_author(name="프리미어리그 일정", icon_url="https://imgsports.pstatic.net/images/2020/pc/common/league/epl_on.png")
                embed2.set_thumbnail(url="https://t1.daumcdn.net/liveboard/sportsvod/200240cbd5354763a69e618f4034e6fe.JPG")
        elif(league == "라리가"):
            schedule_list = Schedule().month_match('primera')
            embed = discord.Embed(title="일정", color=0x00ff56)
            embed.set_author(name="스페인 라리가 일정", icon_url="https://imgsports.pstatic.net/images/2020/pc/common/league/primera_on.png")
            embed.set_thumbnail(url="http://photo.hankooki.com/newsphoto/v001/2020/05/30/upcoming20200530130503_P_02_C_1.jpg")
            embed2.set_author(name="스페인 라리가 일정", icon_url="https://imgsports.pstatic.net/images/2020/pc/common/league/primera_on.png")
            embed2.set_thumbnail(url="http://photo.hankooki.com/newsphoto/v001/2020/05/30/upcoming20200530130503_P_02_C_1.jpg")
        elif(league == "분데스리가"):
            schedule_list = Schedule().month_match('bundesliga')
            embed = discord.Embed(title="일정", color=0x00ff56)
            embed.set_author(name="분데스리가 일정", icon_url="https://imgsports.pstatic.net/images/2020/pc/common/league/bundesliga_on.png")
            embed.set_thumbnail(url="https://e7.pngegg.com/pngimages/489/415/png-clipart-bundesliga-logo-bundesliga-logo-icons-logos-emojis-football.png")
            embed2.set_author(name="분데스리가", icon_url="https://imgsports.pstatic.net/images/2020/pc/common/league/bundesliga_on.png")
            embed2.set_thumbnail(url="https://e7.pngegg.com/pngimages/489/415/png-clipart-bundesliga-logo-bundesliga-logo-icons-logos-emojis-football.png")
        elif(league == "세리에"):
            schedule_list = Schedule().month_match('seria')
            embed = discord.Embed(title="일정", color=0x00ff56)
            embed.set_author(name="이탈리아 세리에 A 일정", icon_url="https://imgsports.pstatic.net/images/2020/pc/common/league/seria_on.png")
            embed.set_thumbnail(url="https://1.bp.blogspot.com/-FuLCBTHRU-U/XWUu9FTnDtI/AAAAAAAAg0g/4Pub1pG2tNQTZlN_wNfcDYKwi0Sevgk_QCLcBGAs/s320/SerieA2019-20LogoOff.png")
            embed2.set_author(name="이탈리아 세리에 A 일정", icon_url="https://imgsports.pstatic.net/images/2020/pc/common/league/seria_on.png")
            embed2.set_thumbnail(url="https://1.bp.blogspot.com/-FuLCBTHRU-U/XWUu9FTnDtI/AAAAAAAAg0g/4Pub1pG2tNQTZlN_wNfcDYKwi0Sevgk_QCLcBGAs/s320/SerieA2019-20LogoOff.png") 
        elif(league == "프랑스리그"):
            schedule_list = Schedule().month_match('ligue1')
            embed = discord.Embed(title="일정", color=0x00ff56)
            embed.set_author(name="프랑스 리그 일정", icon_url="https://imgsports.pstatic.net/images/2020/pc/common/league/ligue1_on.png")
            embed.set_thumbnail(url="https://e7.pngegg.com/pngimages/434/605/png-clipart-2017-18-ligue-1-france-paris-saint-germain-f-c-premier-league-olympique-lyonnais-france-sport-logo.png")
            embed2.set_author(name="프랑스 리그 일정", icon_url="https://imgsports.pstatic.net/images/2020/pc/common/league/ligue1_on.png")
            embed2.set_thumbnail(url="https://e7.pngegg.com/pngimages/434/605/png-clipart-2017-18-ligue-1-france-paris-saint-germain-f-c-premier-league-olympique-lyonnais-france-sport-logo.png")
        elif(league == "챔피언스리그"):
            schedule_list = Schedule().month_match('champs')
            embed = discord.Embed(title="일정", color=0x00ff56)
            embed.set_author(name="챔피언스 리그 일정", icon_url="https://w7.pngwing.com/pngs/819/352/png-transparent-uefa-champions-league-logo-2018-uefa-champions-league-final-uefa-europa-league-europe-2012-uefa-champions-league-final-champions-league-text-sport-team.png")
            embed.set_thumbnail(url="https://www.sports-g.com/wp-content/uploads/2016/08/20160827000261_0-696x624.jpg")
            embed2.set_author(name="챔피언스 리그 일정", icon_url="https://w7.pngwing.com/pngs/819/352/png-transparent-uefa-champions-league-logo-2018-uefa-champions-league-final-uefa-europa-league-europe-2012-uefa-champions-league-final-champions-league-text-sport-team.png")
            embed2.set_thumbnail(url="https://www.sports-g.com/wp-content/uploads/2016/08/20160827000261_0-696x624.jpg")
        elif(league == "유로파리그"):
            schedule_list = Schedule().month_match('europa')
            embed = discord.Embed(title="일정", color=0x00ff56)
            embed.set_author(name="유로파 리그 일정", icon_url="https://t1.daumcdn.net/cfile/tistory/99A58D3E5D84478316")
            embed.set_thumbnail(url="https://t1.daumcdn.net/cfile/tistory/99A58D3E5D84478316")
            embed2.set_author(name="유로파 리그 일정", icon_url="https://t1.daumcdn.net/cfile/tistory/99A58D3E5D84478316")
            embed2.set_thumbnail(url="https://t1.daumcdn.net/cfile/tistory/99A58D3E5D84478316")
        elif(league == "fa컵"):
            schedule_list = Schedule().month_match('facup')
            embed = discord.Embed(title="일정", color=0x00ff56)
            embed.set_author(name="FA컵 일정", icon_url="https://www.betawin.net/wp-content/uploads/2016/12/images.jpg")
            embed.set_thumbnail(url="https://www.betawin.net/wp-content/uploads/2016/12/images.jpg")
            embed2.set_author(name="FA컵 일정", icon_url="https://www.betawin.net/wp-content/uploads/2016/12/images.jpg")
            embed2.set_thumbnail(url="https://www.betawin.net/wp-content/uploads/2016/12/images.jpg")
        else:
            schedule_list = Schedule().month_match()
            embed = discord.Embed(title="일정", color=0x00ff56)
            embed.set_author(name="프리미어리그 일정", icon_url="https://imgsports.pstatic.net/images/2020/pc/common/league/epl_on.png")
            embed.set_thumbnail(url="https://t1.daumcdn.net/liveboard/sportsvod/200240cbd5354763a69e618f4034e6fe.JPG")
            embed2.set_author(name="프리미어리그 일정", icon_url="https://imgsports.pstatic.net/images/2020/pc/common/league/epl_on.png")
            embed2.set_thumbnail(url="https://t1.daumcdn.net/liveboard/sportsvod/200240cbd5354763a69e618f4034e6fe.JPG")
        print(len(schedule_list))
        num = 1
        team_schedule_list = '!'.join(schedule_list)
        print(schedule_list)
        while num < len(schedule_list)/2:
            embed.add_field(name=f"{month}월 {num}일",value=f"```{team_schedule_list.split('!')[num]}```", inline=False)
            num = num + 1
        while num < len(schedule_list):
            embed2.add_field(name=f"{month}월 {num}일",value=f"```{team_schedule_list.split('!')[num]}```", inline=False)
            num = num + 1
        await ctx.send(embed=embed)
        await ctx.send(embed=embed2)

    @commands.command()
    async def 오늘의경기(self, ctx, league='epl'):
        month = datetime.today().month
        day = datetime.today().day
        embed = discord.Embed(title="일정", color=0x00ff56)
        if(league == "프리미어리그"):
                schedule_list = Schedule().today_match()
                embed = discord.Embed(title="일정", color=0x00ff56)
                embed.set_author(name="프리미어리그 일정", icon_url="https://imgsports.pstatic.net/images/2020/pc/common/league/epl_on.png")
                embed.set_thumbnail(url="https://t1.daumcdn.net/liveboard/sportsvod/200240cbd5354763a69e618f4034e6fe.JPG")
        elif(league == "라리가"):
            schedule_list = Schedule().today_match('primera')
            embed = discord.Embed(title="일정", color=0x00ff56)
            embed.set_author(name="스페인 라리가 일정", icon_url="https://imgsports.pstatic.net/images/2020/pc/common/league/primera_on.png")
            embed.set_thumbnail(url="http://photo.hankooki.com/newsphoto/v001/2020/05/30/upcoming20200530130503_P_02_C_1.jpg")
        elif(league == "분데스리가"):
            schedule_list = Schedule().today_match('bundesliga')
            embed = discord.Embed(title="일정", color=0x00ff56)
            embed.set_author(name="분데스리가 일정", icon_url="https://imgsports.pstatic.net/images/2020/pc/common/league/bundesliga_on.png")
            embed.set_thumbnail(url="https://e7.pngegg.com/pngimages/489/415/png-clipart-bundesliga-logo-bundesliga-logo-icons-logos-emojis-football.png")
        elif(league == "세리에"):
            schedule_list = Schedule().today_match('seria')
            embed = discord.Embed(title="일정", color=0x00ff56)
            embed.set_author(name="이탈리아 세리에 A 일정", icon_url="https://imgsports.pstatic.net/images/2020/pc/common/league/seria_on.png")
            embed.set_thumbnail(url="https://1.bp.blogspot.com/-FuLCBTHRU-U/XWUu9FTnDtI/AAAAAAAAg0g/4Pub1pG2tNQTZlN_wNfcDYKwi0Sevgk_QCLcBGAs/s320/SerieA2019-20LogoOff.png")
        elif(league == "프랑스리그"):
            schedule_list = Schedule().today_match('ligue1')
            embed = discord.Embed(title="일정", color=0x00ff56)
            embed.set_author(name="프랑스 리그 일정", icon_url="https://imgsports.pstatic.net/images/2020/pc/common/league/ligue1_on.png")
            embed.set_thumbnail(url="https://e7.pngegg.com/pngimages/434/605/png-clipart-2017-18-ligue-1-france-paris-saint-germain-f-c-premier-league-olympique-lyonnais-france-sport-logo.png")
        elif(league == "챔피언스리그"):
            schedule_list = Schedule().today_match('champs')
            embed = discord.Embed(title="일정", color=0x00ff56)
            embed.set_author(name="챔피언스 리그 일정", icon_url="https://w7.pngwing.com/pngs/819/352/png-transparent-uefa-champions-league-logo-2018-uefa-champions-league-final-uefa-europa-league-europe-2012-uefa-champions-league-final-champions-league-text-sport-team.png")
            embed.set_thumbnail(url="https://www.sports-g.com/wp-content/uploads/2016/08/20160827000261_0-696x624.jpg")
        elif(league == "유로파리그"):
            schedule_list = Schedule().today_match('europa')
            embed = discord.Embed(title="일정", color=0x00ff56)
            embed.set_author(name="유로파 리그 일정", icon_url="https://t1.daumcdn.net/cfile/tistory/99A58D3E5D84478316")
            embed.set_thumbnail(url="https://t1.daumcdn.net/cfile/tistory/99A58D3E5D84478316")
        elif(league == "fa컵"):
            schedule_list = Schedule().today_match('facup')
            embed = discord.Embed(title="일정", color=0x00ff56)
            embed.set_author(name="FA컵 일정", icon_url="https://www.betawin.net/wp-content/uploads/2016/12/images.jpg")
            embed.set_thumbnail(url="https://www.betawin.net/wp-content/uploads/2016/12/images.jpg")
        else:
            schedule_list = Schedule().today_match()
            embed = discord.Embed(title="일정", color=0x00ff56)
            embed.set_author(name="프리미어리그 일정", icon_url="https://imgsports.pstatic.net/images/2020/pc/common/league/epl_on.png")
            embed.set_thumbnail(url="https://t1.daumcdn.net/liveboard/sportsvod/200240cbd5354763a69e618f4034e6fe.JPG")
        print(len(schedule_list))
        team_schedule_list = ''.join(schedule_list)
        print(team_schedule_list)
        embed.add_field(name=f"{month}월 {day}일",value=f"```{team_schedule_list}```", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def 경기(self, ctx, league='epl', year=year, month=month, day=day):
        embed = discord.Embed(title="일정", color=0x00ff56)
        if(league == "프리미어리그"):
            schedule_list = Schedule().this_match('epl',year,month,day)
            embed = discord.Embed(title="일정", color=0x00ff56)
            embed.set_author(name="프리미어리그 일정", icon_url="https://imgsports.pstatic.net/images/2020/pc/common/league/epl_onpng")
            embed.set_thumbnail(url="https://t1.daumcdn.net/liveboard/sportsvod/200240cbd5354763a69e618f4034e6fe.JPG")
        elif(league == "라리가"):
            schedule_list = Schedule().this_match('primera',year,month,day)
            embed = discord.Embed(title="일정", color=0x00ff56)
            embed.set_author(name="스페인 라리가 일정", icon_url="https://imgsports.pstatic.net/images/2020/pc/common/league/primera_on.png")
            embed.set_thumbnail(url="http://photo.hankooki.com/newsphoto/v001/2020/05/30/upcoming20200530130503_P_02_C_1.jpg")
        elif(league == "분데스리가"):
            schedule_list = Schedule().this_match('bundesliga',year,month,day)
            embed = discord.Embed(title="일정", color=0x00ff56)
            embed.set_author(name="분데스리가 일정", icon_url="https://imgsports.pstatic.net/images/2020/pc/common/league/bundesliga_on.png")
            embed.set_thumbnail(url="https://e7.pngegg.com/pngimages/489/415/png-clipart-bundesliga-logo-bundesliga-logo-icons-logos-emojis-football.png")
        elif(league == "세리에"):
            schedule_list = Schedule().this_match('seria',year,month,day)
            embed = discord.Embed(title="일정", color=0x00ff56)
            embed.set_author(name="이탈리아 세리에 A 일정", icon_url="https://imgsports.pstatic.net/images/2020/pc/common/league/seria_on.png")
            embed.set_thumbnail(url="https://1.bp.blogspot.com/-FuLCBTHRU-U/XWUu9FTnDtI/AAAAAAAAg0g/4Pub1pG2tNQTZlN_wNfcDYKwi0Sevgk_QCLcBGAs/s320/SerieA2019-20LogoOff.png")
        elif(league == "프랑스리그"):
            schedule_list = Schedule().this_match('ligue1',year,month,day)
            embed = discord.Embed(title="일정", color=0x00ff56)
            embed.set_author(name="프랑스 리그 일정", icon_url="https://imgsports.pstatic.net/images/2020/pc/common/league/ligue1_on.png")
            embed.set_thumbnail(url="https://e7.pngegg.com/pngimages/434/605/png-clipart-2017-18-ligue-1-france-paris-saint-germain-f-c-premier-league-olympique-lyonnais-france-sport-logo.png")
        elif(league == "챔피언스리그"):
            schedule_list = Schedule().this_match('champs',year,month,day)
            embed = discord.Embed(title="일정", color=0x00ff56)
            embed.set_author(name="챔피언스 리그 일정", icon_url="https://w7.pngwing.com/pngs/819/352/png-transparent-uefa-champions-league-logo-2018-uefa-champions-league-final-uefa-europa-league-europe-2012-uefa-champions-league-final-champions-league-text-sport-team.png")
            embed.set_thumbnail(url="https://www.sports-g.com/wp-content/uploads/2016/08/20160827000261_0-696x624.jpg")
        elif(league == "유로파리그"):
            schedule_list = Schedule().this_match('europa',year,month,day)
            embed = discord.Embed(title="일정", color=0x00ff56)
            embed.set_author(name="유로파 리그 일정", icon_url="https://t1.daumcdn.net/cfile/tistory/99A58D3E5D84478316")
            embed.set_thumbnail(url="https://t1.daumcdn.net/cfile/tistory/99A58D3E5D84478316")
        elif(league == "fa컵"):
            schedule_list = Schedule().this_match('facup',year,month,day)
            embed = discord.Embed(title="일정", color=0x00ff56)
            embed.set_author(name="FA컵 일정", icon_url="https://www.betawin.net/wp-content/uploads/2016/12/images.jpg")
            embed.set_thumbnail(url="https://www.betawin.net/wp-content/uploads/2016/12/images.jpg")
        else:
            schedule_list = Schedule().this_match('epl',year,month,day)
            embed = discord.Embed(title="일정", color=0x00ff56)
            embed.set_author(name="프리미어리그 일정", icon_url="https://imgsports.pstatic.net/images/2020/pc/common/league/epl_on.png")
            embed.set_thumbnail(url="https://t1.daumcdn.net/liveboard/sportsvod/200240cbd5354763a69e618f4034e6fe.JPG")
        print(len(schedule_list))
        team_schedule_list = ''.join(schedule_list)
        print(team_schedule_list)
        embed.add_field(name=f"{month}월 {day}일",value=f"```{team_schedule_list}```", inline=False)
        await ctx.send(embed=embed)