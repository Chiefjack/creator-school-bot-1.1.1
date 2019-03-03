import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
from discord import ChannelType
import asyncio
import random
import datetime
from datetime import timedelta
import os

bot = commands.Bot(command_prefix="cs!")
bot.remove_command("help")
client = discord.Client()

@bot.event
async def on_ready():
	await bot.change_presence(game=discord.Game(name="cs!help for commands", type=0), status=discord.Status("online"))
	message = ("Bot started successfully!")
	user = await bot.get_user_info("284398011310800898")
	await bot.send_message(user, message)
	print(message)
	
@bot.event
async def on_member_join(member):
	message = (f"Welcome {member.mention} to the [OFFICIAL] Creator School! Remember to read the rules and have fun!")
	await bot.send_message(member, message)

#CHANGING TEACHER NEED STATUS

@bot.command(pass_context=True)
@commands.has_role("Staff")
async def blockdeco(ctx):
	message = await bot.get_message(ctx.message.channel, "528221270157033482")
	if ctx.message.content == "cs!blockdeco yes":
		await bot.edit_message(message, "-Block Deco Teachers: *YES*")
	if ctx.message.content == "cs!blockdeco no":
		await bot.edit_message(message, "-Block Deco Teachers: *NO*")

	await bot.delete_message(ctx.message)
		
@bot.command(pass_context=True)
@commands.has_role("Staff")
async def airdeco(ctx):
	message = await bot.get_message(ctx.message.channel, "528221291099062299")
	if ctx.message.content == "cs!airdeco yes":
		await bot.edit_message(message, "-Air Deco Teachers: *YES*")
	if ctx.message.content == "cs!airdeco no":
		await bot.edit_message(message, "-Air Deco Teachers: *NO*")
		
	await bot.delete_message(ctx.message)
		
@bot.command(pass_context=True)
@commands.has_role("Staff")
async def tech(ctx):
	message = await bot.get_message(ctx.message.channel, "528221313114963969")
	if ctx.message.content == "cs!tech yes":
		await bot.edit_message(message, "-Tech Teachers: *YES*")
	if ctx.message.content == "cs!tech no":
		await bot.edit_message(message, "-Tech Teachers: *NO*")
		
	await bot.delete_message(ctx.message)
		
@bot.command(pass_context=True)
@commands.has_role("Staff")
async def glow(ctx):
	message = await bot.get_message(ctx.message.channel, "528221331062390795")
	if ctx.message.content == "cs!glow yes":
		await bot.edit_message(message, "-Glow Teachers: *YES*")
	if ctx.message.content == "cs!glow no":
		await bot.edit_message(message, "-Glow Teachers: *NO*")
		
	await bot.delete_message(ctx.message)
		
@bot.command(pass_context=True)
@commands.has_role("Staff")
async def core(ctx):
	message = await bot.get_message(ctx.message.channel, "528221350515703818")
	if ctx.message.content == "cs!core yes":
		await bot.edit_message(message, "-Core Teachers: *YES*")
	if ctx.message.content == "cs!core no":
		await bot.edit_message(message, "-Core Teachers: *NO*")
		
	await bot.delete_message(ctx.message)
		
@bot.command(pass_context=True)
@commands.has_role("Staff")
async def modern(ctx):
	message = await bot.get_message(ctx.message.channel, "528221369599655946")
	if ctx.message.content == "cs!modern yes":
		await bot.edit_message(message, "-Modern Teachers: *YES*")
	if ctx.message.content == "cs!modern no":
		await bot.edit_message(message, "-Modern Teachers: *NO*")
		
	await bot.delete_message(ctx.message)
		
@bot.command(pass_context=True)
@commands.has_role("Staff")
async def design(ctx):
	message = await bot.get_message(ctx.message.channel, "528221387786289153")
	if ctx.message.content == "cs!design yes":
		await bot.edit_message(message, "-Design Teachers: *YES*")
	if ctx.message.content == "cs!design no":
		await bot.edit_message(message, "-Design Teachers: *NO*")
		
	await bot.delete_message(ctx.message)
		
@bot.command(pass_context=True)
@commands.has_role("Staff")
async def art(ctx):
	message = await bot.get_message(ctx.message.channel, "528221408447430676")
	if ctx.message.content == "cs!art yes":
		await bot.edit_message(message, "-Art Teachers: *YES*")
	if ctx.message.content == "cs!art no":
		await bot.edit_message(message, "-Art Teachers: *NO*")
		
	await bot.delete_message(ctx.message)
		
@bot.command(pass_context=True)
@commands.has_role("Staff")
async def effect(ctx):
	message = await bot.get_message(ctx.message.channel, "528221431671160860")
	if ctx.message.content == "cs!effect yes":
		await bot.edit_message(message, "-Effect Teachers: *YES*")
	if ctx.message.content == "cs!effect no":
		await bot.edit_message(message, "-Effect Teachers: *NO*")
		
	await bot.delete_message(ctx.message)
		
@bot.command(pass_context=True)
@commands.has_role("Staff")
async def gameplay(ctx):
	message = await bot.get_message(ctx.message.channel, "528221449614262301")
	if ctx.message.content == "cs!gameplay yes":
		await bot.edit_message(message, "-Gameplay Teachers: *YES*")
	if ctx.message.content == "cs!gameplay no":
		await bot.edit_message(message, "-Gameplay Teachers: *NO*")
		
	await bot.delete_message(ctx.message)
		
@bot.command(pass_context=True)
@commands.has_role("Staff")
async def trigger(ctx):
	message = await bot.get_message(ctx.message.channel, "528221468862185472")
	if ctx.message.content == "cs!trigger yes":
		await bot.edit_message(message, "-Trigger Teachers: *YES*")
	if ctx.message.content == "cs!trigger no":
		await bot.edit_message(message, "-Trigger Teachers: *NO*")
		
	await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
@commands.has_role("Staff")
async def threedl(ctx):
	message = await bot.get_message(ctx.message.channel, "528221486679326720")
	if ctx.message.content == "cs!threedl yes":
		await bot.edit_message(message, "-3DL Teachers: *YES*")
	if ctx.message.content == "cs!threedl no":
		await bot.edit_message(message, "-3DL Teachers: *NO*")
		
	await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
@commands.has_role("Staff")
async def colour(ctx):
	message = await bot.get_message(ctx.message.channel, "546690051656908800")
	if ctx.message.content == "cs!colour yes":
		await bot.edit_message(message, "-Colour Teachers: *YES*")
	if ctx.message.content == "cs!colour no":
		await bot.edit_message(message, "-Colour Teachers: *NO*")
		
	await bot.delete_message(ctx.message)

#ACCEPTING TEACHERS

@bot.command(pass_context=True)
@commands.has_role("Staff")
async def accept(ctx, user: discord.Member):
	channel = bot.get_channel("435052485065965568")
	request_channel = ctx.message.channel.name
	teacher_type_lower = request_channel.replace("-", " ")
	teacher_type_lower = teacher_type_lower.replace(" application", "")
	teacher_type = teacher_type_lower.title()
	message = ctx.message.content
	accepted_user = message.replace("cs!accept ", "")
	acceptance = (f"User: {accepted_user}\nRequested: {teacher_type}\nAnswer: Yes\nAccepted by: {ctx.message.author.mention}\n*If you would like a reason, please DM {ctx.message.author.mention}.*")
	await bot.send_message(channel, acceptance)

	if teacher_type == "Block Deco":
		teacher_role = get(ctx.message.server.roles, id="414368972272697344")
		applicant_role = get(ctx.message.server.roles, id="528240842352099348")
		await bot.add_roles(user, teacher_role)
		await bot.remove_roles(user, applicant_role)

	if teacher_type == "Air Deco":
		teacher_role = get(ctx.message.server.roles, id="414369150581080074")
		applicant_role = get(ctx.message.server.roles, id="528267301242404874")
		await bot.add_roles(user, teacher_role)
		await bot.remove_roles(user, applicant_role)
		
	if teacher_type == "Tech":
		teacher_role = get(ctx.message.server.roles, id="414367660449595394")
		applicant_role = get(ctx.message.server.roles, id="528267451327184906")
		await bot.add_roles(user, teacher_role)
		await bot.remove_roles(user, applicant_role)
		
	if teacher_type == "Glow":
		teacher_role = get(ctx.message.server.roles, id="414367702371532800")
		applicant_role = get(ctx.message.server.roles, id="528267538103271424")
		await bot.add_roles(user, teacher_role)
		await bot.remove_roles(user, applicant_role)
		
	if teacher_type == "Core":
		teacher_role = get(ctx.message.server.roles, id="414367616778502144")
		applicant_role = get(ctx.message.server.roles, id="528267575222861834")
		await bot.add_roles(user, teacher_role)
		await bot.remove_roles(user, applicant_role)
		
	if teacher_type == "Modern":
		teacher_role = get(ctx.message.server.roles, id="414369109745205248")
		applicant_role = get(ctx.message.server.roles, id="528267616620642321")
		await bot.add_roles(user, teacher_role)
		await bot.remove_roles(user, applicant_role)
		
	if teacher_type == "Design":
		teacher_role = get(ctx.message.server.roles, id="414307474066374656")
		applicant_role = get(ctx.message.server.roles, id="528267680680247303")
		await bot.add_roles(user, teacher_role)
		await bot.remove_roles(user, applicant_role)
		
	if teacher_type == "Art":
		teacher_role = get(ctx.message.server.roles, id="414367762819842053")
		applicant_role = get(ctx.message.server.roles, id="528267733910028321")
		await bot.add_roles(user, teacher_role)
		await bot.remove_roles(user, applicant_role)
		
	if teacher_type == "Effect":
		teacher_role = get(ctx.message.server.roles, id="414730929454710794")
		applicant_role = get(ctx.message.server.roles, id="528267780370464779")
		await bot.add_roles(user, teacher_role)
		await bot.remove_roles(user, applicant_role)
		
	if teacher_type == "Gameplay":
		teacher_role = get(ctx.message.server.roles, id="414894098273796096")
		applicant_role = get(ctx.message.server.roles, id="528267823441641492")
		await bot.add_roles(user, teacher_role)
		await bot.remove_roles(user, applicant_role)
		
	if teacher_type == "Trigger":
		teacher_role = get(ctx.message.server.roles, id="431896062144413696")
		applicant_role = get(ctx.message.server.roles, id="528267870577098756")
		await bot.add_roles(user, teacher_role)
		await bot.remove_roles(user, applicant_role)
		
	if teacher_type == "3DL":
		teacher_role = get(ctx.message.server.roles, id="524184498188058628")
		applicant_role = get(ctx.message.server.roles, id="528267909181734928")
		await bot.add_roles(user, teacher_role)
		await bot.remove_roles(user, applicant_role)
	
	if teacher_type == "Colour":
		teacher_role = get(ctx.message.server.roles, id="546683085823934504")
		applicant_role = get(ctx.message.server.roles, id="546683604735098880")
		await bot.add_roles(user, teacher_role)
		await bot.remove_roles(user, applicant_role)

	role = get(ctx.message.server.roles, id="414808431581462538")
	await bot.add_roles(user, role)
	reminder = (f"Please add ◇ to the front of {user}'s name. Also check that they have the correct Teacher roles as the bot may have had a mishap. Otherwise the bot has done everything else : )")
	await bot.send_message(ctx.message.author, reminder)
	message_to_new_teacher = (f"Congratulations on becoming a {teacher_type} Teacher! Please only post lessons in your class channel, no other messages. Also, once you have taught, please post in #teacher-log the date you have taught, and the class you taught in. Thank you, and well done once again!")
	await bot.send_message(user, message_to_new_teacher)
	
	applicant_stage2_role = get(ctx.message.server.roles, id="527966801158602793")
	await bot.remove_roles(user, applicant_stage2_role)
	
	await bot.say(f"{user.mention} was accepted. Please ignore their request.")
	
	await bot.delete_message(ctx.message)

#DECLINING TEACHERS

@bot.command(pass_context=True)
@commands.has_role("Staff")
async def decline(ctx, user: discord.Member):
	channel = bot.get_channel("435052485065965568")
	request_channel = ctx.message.channel.name
	teacher_type_lower = request_channel.replace("-", " ")
	teacher_type_lower = teacher_type_lower.replace(" application", "")
	teacher_type = teacher_type_lower.title()
	message = ctx.message.content
	declined_user = message.replace("cs!decline ", "")
	decline = (f"User: {declined_user}\nRequested: {teacher_type}\nAnswer: No\nDeclined by: {ctx.message.author.mention}\n*If you would like a reason, please DM {ctx.message.author.mention}. To reapply, please complete the form again. You may need to unreact and react again on the 1st and 2nd stages of the form.*")
	await bot.send_message(channel, decline)
	
	if teacher_type == "Block Deco":
		teacher_role = get(ctx.message.server.roles, id="414368972272697344")
		applicant_role = get(ctx.message.server.roles, id="528240842352099348")
		await bot.remove_roles(user, applicant_role)
		
	if teacher_type == "Air Deco":
		teacher_role = get(ctx.message.server.roles, id="414369150581080074")
		applicant_role = get(ctx.message.server.roles, id="528267301242404874")
		await bot.remove_roles(user, applicant_role)
		
	if teacher_type == "Tech":
		teacher_role = get(ctx.message.server.roles, id="414367660449595394")
		applicant_role = get(ctx.message.server.roles, id="528267451327184906")
		await bot.remove_roles(user, applicant_role)
		
	if teacher_type == "Glow":
		teacher_role = get(ctx.message.server.roles, id="414367702371532800")
		applicant_role = get(ctx.message.server.roles, id="528267538103271424")
		await bot.remove_roles(user, applicant_role)
		
	if teacher_type == "Core":
		teacher_role = get(ctx.message.server.roles, id="414367616778502144")
		applicant_role = get(ctx.message.server.roles, id="528267575222861834")
		await bot.remove_roles(user, applicant_role)
		
	if teacher_type == "Modern":
		teacher_role = get(ctx.message.server.roles, id="414369109745205248")
		applicant_role = get(ctx.message.server.roles, id="528267616620642321")
		await bot.remove_roles(user, applicant_role)
		
	if teacher_type == "Design":
		teacher_role = get(ctx.message.server.roles, id="414307474066374656")
		applicant_role = get(ctx.message.server.roles, id="528267680680247303")
		await bot.remove_roles(user, applicant_role)
		
	if teacher_type == "Art":
		teacher_role = get(ctx.message.server.roles, id="414367762819842053")
		applicant_role = get(ctx.message.server.roles, id="528267733910028321")
		await bot.remove_roles(user, applicant_role)
		
	if teacher_type == "Effect":
		teacher_role = get(ctx.message.server.roles, id="414730929454710794")
		applicant_role = get(ctx.message.server.roles, id="528267780370464779")
		await bot.remove_roles(user, applicant_role)
		
	if teacher_type == "Gameplay":
		teacher_role = get(ctx.message.server.roles, id="414894098273796096")
		applicant_role = get(ctx.message.server.roles, id="528267823441641492")
		await bot.remove_roles(user, applicant_role)
		
	if teacher_type == "Trigger":
		teacher_role = get(ctx.message.server.roles, id="431896062144413696")
		applicant_role = get(ctx.message.server.roles, id="528267870577098756")
		await bot.remove_roles(user, applicant_role)
		
	if teacher_type == "3DL":
		teacher_role = get(ctx.message.server.roles, id="524184498188058628")
		applicant_role = get(ctx.message.server.roles, id="528267909181734928")
		await bot.remove_roles(user, applicant_role)
	
	if teacher_type == "Colour":
		teacher_role = get(ctx.message.server.roles, id="546683085823934504")
		applicant_role = get(ctx.message.server.roles, id="546683604735098880")
		await bot.remove_roles(user, applicant_role)

	applicant_stage2_role = get(ctx.message.server.roles, id="527966801158602793")
	await bot.remove_roles(user, applicant_stage2_role)
	
	await bot.say(f"{user.mention} was declined. Please ignore their request.")
	
	await bot.delete_message(ctx.message)

#SUGGEST COMMAND

@bot.command(pass_context=True)
async def suggest(ctx):
	if ctx.message.channel.id == "528572257774338079":
		message = ctx.message.content
		messagereplace = message.replace("cs!suggest ", "")
		author = ctx.message.author
		suggestion = (f"**NEW SUGGESTION!**\n**USER ID IS:** *{ctx.message.author.id}*\n**TAG IS: *{ctx.message.author.mention}***\n**SUGGESTION IS:** *{messagereplace}*\n---")
		suggestion_channel = bot.get_channel("528573991871447050")
		await bot.send_message(suggestion_channel, suggestion)
		reply = (f"Thanks for your suggestion, {author.mention}! We will look at adding this in the future, thanks for your continued support! This message and your message will be deleted in approx. 30 seconds.")
		send = await bot.send_message(ctx.message.channel, reply)
		await asyncio.sleep(30)
		await bot.delete_message(ctx.message)
		await bot.delete_message(send)
	else:
		correct_channel = bot.get_channel("528572257774338079")
		reply = (f"{ctx.message.author.mention}, please go to {correct_channel.mention} to use this command. This message and your message will be deleted in approx. 30 seconds.")
		send = await bot.send_message(ctx.message.channel, reply)
		await asyncio.sleep(30)
		await bot.delete_message(ctx.message)
		await bot.delete_message(send)

#SUPPORT COMMAND	

@bot.command(pass_context=True)
async def support(ctx):
	if ctx.message.channel.id == "528572257774338079":
		message = ctx.message.content
		messagereplace = message.replace("cs!support", "")
		author = ctx.message.author
		ID = random.randint(1,1000)
		support_req = (f"**NEW SUPPORT REQUEST!**\n**USER ID IS:** *{ctx.message.author.id}*\n**TAG IS: *{ctx.message.author.mention}***\n**SUPPORT ID IS:** *{ID}*\n**REQUEST IS:** {messagereplace}\n---")
		embed = discord.Embed(title="Your Support Request", description=f"Your support request from *{ctx.message.channel.name}*", timestamp=datetime.datetime.utcnow(), inline=False, color=0x00FF00)
		embed.add_field(name="Your Support Message:", value=f"{messagereplace}", inline=False)
		embed.add_field(name=f"Your Support ID is: *{ID}*", value=f"It will be used when someone responds to your request.", inline=False)
		embed.add_field(name="Great News!", value="Your query is being handled!", inline=False)
		embed.set_thumbnail(url=bot.user.avatar_url)
		support_channel = bot.get_channel("528574066710544404")
		await bot.send_message(support_channel, support_req)
		await bot.send_message(author, embed=embed)
		confirm = (f"Your support query has been sent {author.mention}, we'll try and look at it soon. Meanwhile check your DMs for more info! This message and your message will be deleted in approx. 30 seconds.")
		send = await bot.send_message(ctx.message.channel, confirm)
		await asyncio.sleep(30)
		await bot.delete_message(ctx.message)
		await bot.delete_message(send)
	else:
		correct_channel = bot.get_channel("528572257774338079")
		reply = (f"{ctx.message.author.mention}, please go to {correct_channel.mention} to use this command. This message and your message will be deleted in approx. 30 seconds.")
		send = await bot.send_message(ctx.message.channel, reply)
		await asyncio.sleep(30)
		await bot.delete_message(ctx.message)
		await bot.delete_message(send)

@bot.command(pass_context=True)
@commands.has_role("Staff")
async def supportresponse(ctx, member: discord.Member):
	message = ctx.message.content
	messagereplace = message.replace("cs!supportresponse", "")
	embed = discord.Embed(title="Your Support Request", description=f"Your support request is complete!", timestamp=datetime.datetime.utcnow(), inline=False, color=0x00FF00)
	embed.add_field(name="Great News!", value="**Your query has a response!**\n"
											 f"Response from *{ctx.message.author}*, who says:\n"
											 f"{messagereplace}", inline=False)
	embed.set_thumbnail(url=bot.user.avatar_url)
	await bot.send_message(member, embed=embed)

#HELP COMMAND

@bot.command(pass_context=True)
async def help(ctx):
	embed = discord.Embed(title="**COMMANDS**", description="This bots commands are shown below (the prefix is cs!)"
															"\n---", color=0x00ff00)
	embed.add_field(name="**PUBLIC COMMANDS**", value= "**cs!help** - Displays this message for the list of bot commands\n"
													 "**cs!support** - Have a question or query about the server or bot? Just ask after cs!support\n"
													 "**cs!suggest** - Have a suggestion for the server or bot? Just tell us after cs!suggest\n"
													 "**cs!ping** - Checks and returns the bots ping\n"
													 "**cs!format** - Displays the teacher application format\n"
													 "**cs!tutor** - Request a tutor for you desired class. Type cs!tutor <class name here>. See pinned message in #private-tutoring\n"
													 "**cs!teacherrate** - Rate a teacher out of 10 (it is anonymous). Type cs!teacherrate <tag teacher> <score out of 10>. EG. cs!teacherrate @ChiefJack_YT#4450 10\n"
													 "**cs!tutorrate** - Rate a tutor out of 10 (it is anonymous). Type cs!tutorrate <tag tutor> <score out of 10>. EG. cs!tutorrate @ChiefJack_YT#4450 10\n"
													 "**cs!report** - Report a user. Type cs!report <tag user> <reason/proof>. If you need to send image proof, please DM that straight to a Staff member, ideally the owner as unforunately the bot doesn't support the sending of images. EG. cs!report @ChiefJack_YT#4450 Being the Owner\n"
													 "---")
	embed.add_field(name="**STAFF COMMANDS**", value= "**cs!staffhelp** - Use this for the list of Staff commands and how to use them\n"
													"---")
	embed.set_thumbnail(url=bot.user.avatar_url)
	await bot.say(embed=embed)

@bot.command(pass_context=True)
@commands.has_role("Staff")
async def staffhelp(ctx):
	embed = discord.Embed(title="**COMMANDS**", description="This bots commands are shown below (the prefix is cs!)"
															"\n---", color=0x00ff00)
	embed.add_field(name="**STAFF COMMANDS**", value= "**cs!supportresponse** - Responds to support requests. See pinned message in #support-log\n"
													"**cs![class name] [yes/no]** - Toggles whether we are accepting certain teachers. See #bot-support for more details\n"
													"**cs!accept [tag user]** - Accepts the tagged user as a teacher for the teacher application channel this is used in\n"
													"**cs!decline [tag user]** - Declines the tagged user as a teacher for the teacher application channel this is used in\n"
													"**cs!tutorresponse** - Reply to a tutor request. See pinned message in #tutor-request-log\n"
													"**cs!reportresponse** - Reply to a user report. See pinned message in #user-reports\n"
													"---")
	embed.set_thumbnail(url=bot.user.avatar_url)
	await bot.say(embed=embed)

#MISC

@bot.command(pass_context=True)
async def ping(ctx):
	message1 = await bot.say(":ping_pong: Pong! Loading...")
	difference = message1.timestamp - ctx.message.timestamp
	await bot.edit_message(message1, f":ping_pong: Pong! That took {1000*difference.total_seconds():.1f}ms.")

@bot.command(pass_context=True)
async def format(ctx):
	if ctx.message.channel.id == "528215464136933387":
		channel = True
	elif ctx.message.channel.id == "528265872008019969":
		channel = True
	elif ctx.message.channel.id == "528266014358503466":
		channel = True
	elif ctx.message.channel.id == "528266063503294484":
		channel = True
	elif ctx.message.channel.id == "528266105702318101":
		channel = True
	elif ctx.message.channel.id == "528266173280681994":
		channel = True
	elif ctx.message.channel.id == "528266221729349642":
		channel = True
	elif ctx.message.channel.id == "528266267266646036":
		channel = True
	elif ctx.message.channel.id == "528266333654351882":
		channel = True
	elif ctx.message.channel.id == "528266397340663808":
		channel = True
	elif ctx.message.channel.id == "528266444182388765":
		channel = True
	elif ctx.message.channel.id == "528266496711852035":
		channel = True
	elif ctx.message.channel.id == "546684101420253184":
		channel = True
	else:
		await bot.say("You can only use this command in a teacher application channel.")
	
	if channel == True:
		await bot.say("**This is the format for requesting a teacher role:**\n\n"
					  "Requesting Teacher: *[teacher type you're requesting]*\n"
					  "Tutor for this class? (helping students via DM): *[yes/no]*\n"
					  "Skills: *[skills in this subject]*\n"
					  "Weaknesses: *[weaknesses in this subject]*\n"
					  "Works: *[at least 2 photos or videos showcasing your work, if you are requesting gameplay you can leave a level ID if it is under 7 stars]*")

#REQUESTING TUTORING

@bot.command(pass_context=True)
async def tutor(ctx):
	if ctx.message.channel.id == "543775636959789056":
		message = ctx.message.content
		messagereplace = message.replace("cs!tutor", "")
		author = ctx.message.author
		ID = random.randint(1,1000)
		tutor_req = (f"**NEW TUTOR REQUEST!**\n**USER ID IS:** *{ctx.message.author.id}*\n**TAG IS: *{ctx.message.author.mention}***\n**TUTOR REQUEST ID IS:** *{ID}*\n**CLASS REQUESTED IS:** {messagereplace}\n---")
		embed = discord.Embed(title="Your Tutor Request", description=f"Your tutor request from *{ctx.message.channel.name}*", timestamp=datetime.datetime.utcnow(), inline=False, color=0x00FF00)
		embed.add_field(name="Your Class Requested For Tutoring:", value=f"{messagereplace}", inline=False)
		embed.add_field(name=f"Your Tutor Request ID is: *{ID}*", value=f"It will be used when someone responds to your request.", inline=False)
		embed.add_field(name="Great News!", value="Your request is being handled!", inline=False)
		embed.set_thumbnail(url=bot.user.avatar_url)
		request_channel = bot.get_channel("544141539597746186")
		await bot.send_message(request_channel, tutor_req)
		await bot.send_message(author, embed=embed)
		confirm = (f"Your tutor request has been sent {author.mention}, we'll try and look at it soon. Meanwhile check your DMs for more info! This message and your message will be deleted in approx. 30 seconds.")
		send = await bot.send_message(ctx.message.channel, confirm)
		await asyncio.sleep(30)
		await bot.delete_message(ctx.message)
		await bot.delete_message(send)
	else:
		correct_channel = bot.get_channel("543775636959789056")
		reply = (f"{ctx.message.author.mention}, please go to {correct_channel.mention} to use this command. This message and your message will be deleted in approx. 30 seconds.")
		send = await bot.send_message(ctx.message.channel, reply)
		await asyncio.sleep(30)
		await bot.delete_message(ctx.message)
		await bot.delete_message(send)

@bot.command(pass_context=True)
@commands.has_any_role("◆ - Tutors", "Staff")
async def tutorresponse(ctx, member: discord.Member):
	message = ctx.message.content
	messagereplace = message.replace("cs!tutorresponse", "")
	embed = discord.Embed(title="Your Tutor Request", description=f"Your tutor request is complete!", timestamp=datetime.datetime.utcnow(), inline=False, color=0x00FF00)
	embed.add_field(name="Great News!", value="**Your tutor request has a response!**\n"
											 f"Response from *{ctx.message.author}*, who says:\n"
											 f"{messagereplace}", inline=False)
	embed.set_thumbnail(url=bot.user.avatar_url)
	await bot.send_message(member, embed=embed)
	reminder = (f"You are now {member}'s tutor for the style they requested. Please DM them when tutoring, and DM them a welcome message!")
	await bot.send_message(ctx.message.author, reminder)

#TEACHER RATE

@bot.command(pass_context=True)
async def teacherrate(ctx, member: discord.Member):
	message = ctx.message.content
	messagereplace = message.replace("cs!teacherrate", "")
	teacher_rate = (f"**NEW TEACHER RATING!**\n**TEACHER IS:** {member.mention}\n**RATING IS:** {messagereplace}/10\n---")
	teacher_rate_channel = bot.get_channel("544201403959214090")
	await bot.send_message(teacher_rate_channel, teacher_rate)
	await bot.say(f"Your Teacher rating has been submitted successfully, {ctx.message.author.mention}!")

#TUTOR RATE

@bot.command(pass_context=True)
async def tutorrate(ctx, member: discord.Member):
	message = ctx.message.content
	messagereplace = message.replace("cs!tutorrate", "")
	tutor_rate = (f"**NEW TUTOR RATING!**\n**TUTOR IS:** {member.mention}\n**RATING IS:** {messagereplace}/10\n---")
	tutor_rate_channel = bot.get_channel("544201584658350091")
	await bot.send_message(tutor_rate_channel, tutor_rate)
	await bot.say(f"Your Tutor rating has been submitted successfully!, {ctx.message.author.mention}")

#USER REPORT

@bot.command(pass_context=True)
async def report(ctx, member: discord.Member):
	message = ctx.message.content
	messagereplace = message.replace("cs!report", "")
	author = ctx.message.author
	ID = random.randint(1,1000)
	report = (f"**NEW USER REPORT!**\n**USER ID IS:** *{member.id}*\n**TAG IS: *{member.mention}***\n**REPORTER USER ID IS:** *{ctx.message.author.id}*\n**REPORTER IS: *{ctx.message.author.mention}***\n**REPORT ID IS:** *{ID}*\n**REPORT IS:** {messagereplace}\n---")
	embed = discord.Embed(title="Your User Report", description=f"Your user report from *{ctx.message.channel.name}*", timestamp=datetime.datetime.utcnow(), inline=False, color=0x00FF00)
	embed.add_field(name="Your User Report:", value=f"{messagereplace}", inline=False)
	embed.add_field(name=f"Your Report ID is: *{ID}*", value=f"It will be used when someone responds to your report.", inline=False)
	embed.add_field(name="Great News!", value="Your report is being handled!", inline=False)
	embed.set_thumbnail(url=bot.user.avatar_url)
	report_channel = bot.get_channel("544206000467738626")
	await bot.send_message(report_channel, report)
	await bot.send_message(author, embed=embed)
	confirm = (f"Your user report has been sent {author.mention}, we'll try and look at it soon. Meanwhile check your DMs for more info! This message and your message will be deleted in approx. 30 seconds.")
	send = await bot.send_message(ctx.message.channel, confirm)
	await asyncio.sleep(30)
	await bot.delete_message(ctx.message)
	await bot.delete_message(send)

@bot.command(pass_context=True)
async def reportresponse(ctx, member: discord.Member):
	message = ctx.message.content
	messagereplace = message.replace("cs!reportresponse", "")
	embed = discord.Embed(title="Your User Report", description=f"Your user report is complete!", timestamp=datetime.datetime.utcnow(), inline=False, color=0x00FF00)
	embed.add_field(name="Great News!", value="**Your user report has a response!**\n"
											 f"Response from *{ctx.message.author}*, who says:\n"
											 f"{messagereplace}", inline=False)
	embed.set_thumbnail(url=bot.user.avatar_url)
	await bot.send_message(member, embed=embed)

bot.run(os.environ["TOKEN"])