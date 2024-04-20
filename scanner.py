import requests
import re
import ssl
import time
import os
import socket
from colorama import Fore, Style

def display_scanner_screen(url):
    """
    Display scanner screen for the provided URL.
    """
    os.system('clear')

def verificar_dns(url):
    try:
        domain = url.split("//")[-1].split("/")[0]
        ip_address = puxar_ip(url)
        if ip_address:
            return f"{Fore.GREEN}DNS Resolvido:{Style.RESET_ALL} {domain} => {ip_address}"
        else:
            return f"{Fore.RED}Erro ao resolver DNS.{Style.RESET_ALL}"
    except Exception:
        return f"{Fore.RED}Erro ao verificar DNS.{Style.RESET_ALL}"

def verificar_firewall(url):
    try:
        response = requests.head(url)
        firewall_info = response.headers.get("X-Firewall", "Não disponível")
        if firewall_info.lower() == "closed":
            return f"{Fore.RED}Firewall fechado{Style.RESET_ALL}"
        elif firewall_info.lower() == "open":
            return f"{Fore.GREEN}Firewall aberto{Style.RESET_ALL}"
        else:
            return f"{Fore.YELLOW}{firewall_info}{Style.RESET_ALL}"
    except requests.RequestException as e:
        return f"{Fore.RED}Erro ao verificar o firewall: {str(e)}{Style.RESET_ALL}"

def obter_versao_servidor(url):
    try:
        response = requests.get(url)
        server_version = response.headers.get("Server", "Não disponível")
        return f"{Fore.CYAN}Versão do servidor web:{Style.RESET_ALL} {server_version}"
    except requests.RequestException as e:
        return f"{Fore.RED}Erro ao obter a versão do servidor: {str(e)}{Style.RESET_ALL}"

def puxar_ip(url):
    try:
        domain = url.split("//")[-1].split("/")[0]
        ip_address = socket.gethostbyname(domain)
        return f"{Fore.YELLOW}IP:{Style.RESET_ALL} {ip_address}"
    except socket.gaierror:
        return f"{Fore.RED}IP não encontrado.{Style.RESET_ALL}"

def verificar_disponibilidade(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        return False
    except requests.RequestException:
        return False

def verificar_robots_txt(url):
    robots_url = f"{url}/robots.txt"
    try:
        response = requests.get(robots_url)
        if response.status_code == 200:
            return response.text
        return f"{Fore.RED}Arquivo robots.txt não encontrado.{Style.RESET_ALL}"
    except requests.RequestException:
        return f"{Fore.RED}Erro ao acessar robots.txt.{Style.RESET_ALL}"

def verificar_tempo_de_carregamento(url):
    try:
        start_time = time.time()
        response = requests.get(url)
        end_time = time.time()
        load_time = end_time - start_time
        return f"{Fore.YELLOW}Tempo de carregamento:{Style.RESET_ALL} {load_time:.2f} segundos"
    except requests.RequestException:
        return f"{Fore.RED}Erro ao medir o tempo de carregamento.{Style.RESET_ALL}"

def verificar_ssl_tls(url):
    try:
        hostname = url.split("//")[-1].split("/")[0]
        ctx = ssl.create_default_context()
        s = ctx.wrap_socket(socket.socket(), server_hostname=hostname)
        s.connect((hostname, 443))
        cert = s.getpeercert()
        if cert:
            return f"{Fore.GREEN}Certificado SSL/TLS válido.{Style.RESET_ALL}"
        else:
            return f"{Fore.YELLOW}Certificado SSL/TLS inválido.{Style.RESET_ALL}"
    except Exception as e:
        return f"{Fore.RED}Erro ao verificar SSL/TLS: {str(e)}{Style.RESET_ALL}"


def verificar_servicos_adicionais(url, portas):
    try:
        host = url.split("//")[-1].split("/")[0]
        servicos_disponiveis = []
        for porta in portas:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            resultado = sock.connect_ex((host, porta))
            sock.close()
            if resultado == 0:
                servicos_disponiveis.append(porta)
        return servicos_disponiveis
    except Exception:
        return f"{Fore.RED}Erro ao verificar serviços adicionais.{Style.RESET_ALL}"

def exibir_dados_do_site_e_portas_abertas(url):
    if not (url.startswith("http://") or url.startswith("https://")):
        url = "http://" + url

    portas_comuns = [21, 22, 23, 25, 53, 80, 443, 3306, 8080]

    print(f"\n{Fore.CYAN}DADOS DO SITE:{Style.RESET_ALL} {url}")
    if verificar_disponibilidade(url):
        print(f"{Fore.GREEN}O site está online.{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}O site não está disponível.{Style.RESET_ALL}")

    ip = puxar_ip(url)
    if ip:
        print(ip)
    else:
        print(f"{Fore.RED}IP não encontrado.{Style.RESET_ALL}")

    robots_txt = verificar_robots_txt(url)
    print(robots_txt)

    load_time = verificar_tempo_de_carregamento(url)
    print(load_time)

    ssl_info = verificar_ssl_tls(url)
    print(ssl_info)

    servicos_disponiveis = verificar_servicos_adicionais(url, portas_comuns)
    if isinstance(servicos_disponiveis, list) and len(servicos_disponiveis) > 0:
        print(f"{Fore.GREEN}Serviços adicionais disponíveis nas portas:{Style.RESET_ALL} {servicos_disponiveis}")
    else:
        print(f"{Fore.YELLOW}Nenhum serviço adicional disponível nas portas comuns.{Style.RESET_ALL}")

    urls_verificar = [
        "/admin", "/login", "/register", "/wp-admin", "/contact",
        "/about", "/terms", "/privacy", "/services", "/blog",
        "/faq", "/shop", "/products", "/portfolio", "/pricing",
        "/news", "/events", "/gallery", "/testimonials", "/clients",
        "/team", "/careers", "/download", "/feedback", "/sitemap",
        "/error", "/subscribe", "/unauthorized", "/dashboard", "/members",
        "/logout", "/account", "/contact.php", "/fotos.php", "/videos", "/podcasts", "/partnerships", "/guest-posts", "/customer-stories",
        "/daily-deals", "/recent-projects", "/local-events", "/success-stories", "/social-media",
        "/user-forum", "/job-openings", "/official-blog", "/photo-gallery", "/our-team",
        "/product-reviews", "/client-reviews", "/support-center", "/terms-of-service", "/privacy-policy",
        "/cookie-policy", "/community-forum", "/how-it-works", "/meet-the-team", "/behind-the-scenes",
        "/awards-and-recognition", "/our-values", "/why-choose-us", "/charity-work", "/news-and-updates",
        "/help-center", "/recent-news",
        "/webinars", "/ebooks", "/whitepapers", "/case-studies", "/press-releases",
        "/media-kit", "/affiliate-program", "/donate", "/volunteer", "/internships",
        "/scholarships", "/grants", "/contests", "/surveys", "/webcasts",
        "/podcast-episodes", "/video-tutorials", "/infographics", "/guides", "/reports",
        "/rss-feed", "/xml-sitemap", "/json-sitemap", "/robots.txt", "/ads.txt",
        "/.well-known/security.txt", "/.well-known/dnt-policy.txt", "/.well-known/assetlinks.json", "/.well-known/apple-app-site-association",
        "/api", "/api-docs", "/api/v1", "/api/v2", "/api/login", "/api/logout", "/api/register", "/api/data", "/api/config",
        "/api/user", "/api/admin", "/api/info", "/api/update", "/api/delete", "/api/create", "/api/test", "/api/dev", "/api/status",
        "/api/help", "/api/settings", "/api/support", "/api/version", "/api/download", "/api/upload", "/api/content", "/api/search",
        "/api/auth", "/api/account", "/api/profile", "/api/notification", "/api/feedback", "/api/report", "/api/analysis", "/api/dashboard",
        "/api/resources", "/api/assets", "/api/images", "/api/files", "/api/videos", "/api/audios", "/api/texts", "/api/documents",
        "/api/categories", "/api/tags", "/api/comments", "/api/reviews", "/api/ratings", "/api/likes", "/api/followers", "/api/following",
        "/api/messages", "/api/chats", "/api/threads", "/api/posts", "/api/articles", "/api/pages", "/api/items", "/api/products",
        "/api/orders", "/api/cart", "/api/checkout", "/api/payments", "/api/invoices", "/api/shipments", "/api/returns", "/api/refunds",
        "/api/coupons", "/api/discounts", "/api/sales", "/api/tickets", "/api/events", "/api/sessions", "/api/webinars", "/api/courses",
        "/api/lessons", "/api/exams", "/api/questions", "/api/answers", "/api/submissions", "/api/grades", "/api/certificates", "/api/achievements",
        "/api/progress", "/api/goals", "/api/tasks", "/api/projects", "/api/jobs", "/api/applications", "/api/interviews", "/api/offers",
        "/api/employees", "/api/employers", "/api/clients", "/api/vendors", "/api/partners", "/api/investors", "/api/sponsors", "/api/donors",
        "/api/volunteers", "/api/members", "/api/users", "/api/people", "/api/students", "/api/teachers", "/api/professors", "/api/researchers",
        "/api/doctors", "/api/nurses", "/api/patients", "/api/lawyers", "/api/judges", "/api/defendants", "/api/plaintiffs", "/api/witnesses",
        "/api/officers", "/api/soldiers", "/api/civilians", "/api/citizens", "/api/residents", "/api/visitors", "/api/guests", "/api/hosts",
        "/api/owners", "/api/tenants", "/api/drivers", "/api/passengers", "/api/pilots", "/api/flight-attendants", "/api/travelers", "/api/tourists",
        "/api/guides", "/api/chefs", "/api/waiters", "/api/bartenders", "/api/customers", "/api/consumers", "/api/users", "/api/creators",
        "/api/designers", "/api/developers", "/api/engineers", "/api/scientists", "/api/writers", "/api/editors", "/api/photographers", "/api/filmmakers",
        "/api/actors", "/api/directors", "/api/producers", "/api/musicians", "/api/singers", "/api/dancers", "/api/artists", "/api/painters",
        "/api/sculptors", "/api/architects", "/api/builders", "/api/carpenters", "/api/plumbers", "/api/electricians", "/api/mechanics", "/api/drivers",
        "/api/gardeners", "/api/farmers", "/api/ranchers", "/api/fishermen", "/api/hunters", "/api/miners", "/api/loggers", "/api/traders",
        "/api/brokers", "/api/dealers", "/api/agents", "/api/advisors", "/api/consultants", "/api/coaches", "/api/trainers", "/api/mentors",
        "/api/therapists", "/api/counselors", "/api/social-workers", "/api/caregivers", "/api/nannies", "/api/maids", "/api/cooks", "/api/cleaners",
        "/api/security-guards", "/api/police-officers", "/api/firefighters", "/api/paramedics", "/api/lifeguards", "/api/rescue-workers", "/api/volunteers", "/api/helpers"
    ]

    dns_info = verificar_dns(url)
    print(dns_info)
    firewall_status = verificar_firewall(url)
    print(f"{Fore.CYAN}Informações do firewall:{Style.RESET_ALL} {firewall_status}")
    server_version = obter_versao_servidor(url)
    print(server_version)
    for url_verificar in urls_verificar:
        url_completa = f"{url}{url_verificar}"
        if verificar_disponibilidade(url_completa):
            print(f"{Fore.GREEN}URL {url_verificar} encontrada no site.{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}URL {url_verificar} não encontrada no site.{Style.RESET_ALL}")