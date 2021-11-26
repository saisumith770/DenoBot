async def helper_command(channel):
    await channel.send('''`
        !deno commands
        !deno help
        !deno invites
        !deno invite_info <invite code>
    `''')