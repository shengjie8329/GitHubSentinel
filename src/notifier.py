import smtplib
import markdown2
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from logger import LOG

class Notifier:
    def __init__(self, email_settings):
        self.email_settings = email_settings
    
    def notify(self, repo, report):
        if self.email_settings:
            self.send_email(repo, report)
        else:
            LOG.warning("邮件设置未配置正确，无法发送通知")
    
    def send_email(self, repo, report):
        LOG.info("准备发送邮件")
        msg = MIMEMultipart()
        msg['From'] = self.email_settings['from']
        msg['To'] = self.email_settings['to']
        msg['Subject'] = f"{repo} 进展简报"
        
        # 将Markdown内容转换为HTML
        html_report = markdown2.markdown(report)

        msg.attach(MIMEText(html_report, 'html'))
        try:
            with smtplib.SMTP_SSL(self.email_settings['smtp_server'], self.email_settings['smtp_port']) as server:
                LOG.debug("登录SMTP服务器")
                server.login(msg['From'], self.email_settings['password'])
                server.sendmail(msg['From'], msg['To'], msg.as_string())
                LOG.info("邮件发送成功！")
        except Exception as e:
            LOG.error(f"发送邮件失败：{str(e)}")

if __name__ == '__main__':
    from config import Config
    config = Config()
    notifier = Notifier(config.email)

    test_repo = "[HackNews] 最新简报"
    test_report = """
# Hacker News 技术洞察

## 时间：2024年8月28日

## 技术前沿趋势与热点话题

1. **实时游戏引擎创新**：GameNGen的发布引起关注，这是一种完全由神经网络模型驱动的实时游戏引擎。它的出现标志着游戏开发领域在利用深度学习和生成模型方面的突破，可能会改变游戏的开发和体验方式。

2. **Mono项目的未来**：Microsoft将Mono项目移交给Wine团队，引发关于开源项目未来方向的讨论。Mono作为.NET生态系统的重要组成部分，它的继承与发展将影响跨平台开发者社区的未来。

3. **COSMIC桌面环境的推出**：System76发布了COSMIC的Alpha版本，该桌面环境得到Linux用户的高度关注。其个性化和高效设计受到了赞誉，预示着开源桌面环境正朝着更加现代化的方向发展。

4. **加强Linux应用管理的工具**：Boxxy工具的发布，允许用户对不适当的Linux应用进行管控，展示了对用户环境的更精细控制。它的工作方式通过重定向配置文件存储位置来改善用户体验，这提供了更加灵活的配置管理方案。

5. **特斯拉的新TTPoE协议**：特斯拉在Hot Chips 2024上介绍了TTPoE，这是一种替代TCP的低延迟协议。该协议致力于提升超级计算机Dojo的通信效率，展示了如何通过硬件与软件的结合来优化数据传输，对于高性能计算领域的影响深远。

"""
    notifier.notify(test_repo, test_report)
