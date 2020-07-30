from discord.ext import commands
from modules import rank
import discord

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

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

