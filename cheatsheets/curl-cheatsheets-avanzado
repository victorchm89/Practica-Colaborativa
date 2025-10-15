
# Cheatsheet avanzada de `curl` para análisis ofensivo

Esta cheatsheet cubre técnicas avanzadas con `curl` para testeo de aplicaciones web, APIs y automatización de pruebas ofensivas.

---

## Ver código fuente de una web

```bash
curl http://target.com
````

---

## Inyección XSS Reflejado

```bash
curl "http://target.com/search.php?q=<script>alert(1)</script>"
```

---

## Envío de cabeceras personalizadas

```bash
curl -H "X-Forwarded-For: 127.0.0.1" http://target.com/admin
```

---

## Autenticación con token (JWT / Bearer)

```bash
curl -H "Authorization: Bearer <token>" http://target.com/api/user
```

---

## Petición POST (login)

```bash
curl -X POST -d "user=admin&pass=1234" http://target.com/login.php
```

---

## Subida de archivo (bypass de tipo MIME)

```bash
curl -F "file=@evil.php.jpg" http://target.com/upload.php
```

---

## Uso con proxy (Burp, Zap…)

```bash
curl --proxy http://127.0.0.1:8080 http://target.com
```

---

## Enviar cookies manualmente

```bash
curl --cookie "sessionid=abc123" http://target.com/dashboard
```

---

## Ver solo cabeceras (HEAD request)

```bash
curl -I http://target.com
```

---

## Fuzzing básico con wordlist (Bash loop)

```bash
for i in $(cat wordlist.txt); do
  curl http://target.com/$i
done
```

---

## Limpiar salida HTML con lynx (solo texto plano)

```bash
curl http://target.com | lynx -dump -
```
