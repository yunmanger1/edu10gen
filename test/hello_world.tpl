<!DOCTYPE html>
<html>
<head>
    <title>Hello World!</title>
</head>
<body>
    Hello, {{ username }}!
<ul>
%for item in things:
    <li>{{ item }}</li>
%end
</ul>
</body>
</html>