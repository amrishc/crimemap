<VirtualHost *>
    Servername accrimemap.com

    WSGIScriptAlias / /var/www/crimemap/crimemap.wsgi
    WSGIDaemonProcess crimemap
    <Directory /var/www/crimemap>
        WSGIProcessGroup crimemap
        WSGIApplicationGroup %{GLOBAL}%
            Order deny,allow
            Allow from all
    </Directory>
</VirtualHost>