*DOMAIN
webtob1

*NODE
@@host_name@@	WEBTOBDIR="/root/webtob", 
		SHMKEY = 54000,
		DOCROOT="/root/webtob/docs",
		PORT = "80", 
		HTH = 1,
		#Group = "nobody",
		#User = "nobody",
		NODENAME = "$(NODENAME)",
        ERRORDOCUMENT = "503",
        Options="INDEX",
        LOGGING = "log1",
        ERRORLOG = "log2",
        SYSLOG = "syslog",
        JSVPORT = 9900,
        DIRINDEX = "dindex",
        METHOD = "PUT,DELETE",
        LimitRequestBody=8589934592

*DIRINDEX
dindex
        Options = "+Fancy"
*HTH_THREAD
hth_worker
                  SendfileThreads = 4,
                  AccessLogThread = Y,
                  #ReadBufSize=1048576, #1M
                  #HtmlsCompression="text/html",
                  #SendfileThreshold=32768,
                  WorkerThreads=8

*SVRGROUP
htmlg           NODENAME = "@@host_name@@", SVRTYPE = HTML
cgig            NODENAME = "@@host_name@@", SVRTYPE = CGI
ssig            NODENAME = "@@host_name@@", SVRTYPE = SSI
jsvg            NODENAME = "@@host_name@@", SVRTYPE = JSV


*SERVER
cgi		SVGNAME = cgig, MinProc = 2, MaxProc = 10, ASQCount = 1 
ssi 		SVGNAME = ssig, MinProc = 2, MaxProc = 10, ASQCount = 1
MyGroup         SVGNAME = jsvg, MinProc = 2, MaxProc = 10


*URI
uri1		Uri = "/cgi-bin/",   Svrtype = CGI
uri2            Uri = "/examples/",  SvrType=JSV, SvrName=MyGroup


*ALIAS
alias1		URI = "/cgi-bin/", RealPath = "/root/webtob/cgi-bin/"

*LOGGING
syslog		Format = "SYSLOG", FileName = "/root/webtob/log/system.log_%M%%D%%Y%",
			Option = "sync"
log1		Format = "DEFAULT", FileName = "/root/webtob/log/access.log_%M%%D%%Y%", 
			Option = "sync"
log2		Format = "ERROR", FileName = "/root/webtob/log/error.log_%M%%D%%Y%", 
			Option = "sync"

*ERRORDOCUMENT
503			status = 503,
			url = "/503.html"

*EXT
jsp             Mimetype ="application/jsp",  Svrtype=JSV,  SvrName=MyGroup

