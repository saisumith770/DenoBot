async def helper_command(channel):
    await channel.send('''`
        !deno commands
        !deno help
        !deno invites
        !deno invite_info <invite code | invite url>
        !deno add_invite <channel name>(optional) <age,uses,temporary>(optional)
        !deno remove_invite <invite code | invite url>(optional)
    `''')