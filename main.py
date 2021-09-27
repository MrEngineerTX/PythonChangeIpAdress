from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy,ProxyType
import time 


proxy_ip_port = "proxy_ip : port_number"
proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = proxy_ip_port
proxy.ssl_proxy  = proxy_ip_port

capabilities = webdriver.DesiredCapabilities.CHROME
proxy.add_to_capabilities(capabilities)

driver = webdriver.Chrome("chromedriver.exe",desired_capabilities=capabilities)
driver.get("https://httpbin.org/ip")
