var http = require('http');
var fs = require('fs');
var url = require('url');
var qs = require('querystring');
function templateHTML(path){
    data = fs.readFileSync(path,'utf-8');
    return data;
}

var app = http.createServer(function(request,response){
    var _url = request.url;
    var pathname = url.parse(_url,true).pathname;
    if(pathname == '/'){
         response.writeHead(200);
         response.end(templateHTML('./html/sign_in/index.html'));
    }
})

app.listen(3001);