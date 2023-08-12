import send
import receive
import re
import qwen
botQQ = botQQNum#整形数，不是字符串
if __name__ == "__main__":
    while True:
        rev = receive.rev_msg()
        if rev['post_type'] == 'message':
            msgType = rev['message_type']
            msgContent = rev['message']
            if msgType == 'private':#私聊
                qqNum = rev['user_id']
                answer = qwen.chat(msgContent,qqNum)
                send.send_msg({'msg_type':msgType,'number':qqNum,'msg':answer})
            else:#群聊
                if msgContent.startswith("[CQ:"):
                    match = re.match(r"\[CQ:at,qq=(\d+)\]",msgContent)
                    if match:
                        qqNum_at = match.group(1)
                        if qqNum_at != str(botQQ):
                            continue
                else:
                    continue
                split_string = msgContent.split()
                content = "".join(split_string[1:]) if len(split_string) > 1 else ""
                groupNum = rev['group_id']
                answer = qwen.chat(msgContent,groupNum)
                send.send_msg({'msg_type':msgType,'number':groupNum,'msg':answer})
        else:
            continue
