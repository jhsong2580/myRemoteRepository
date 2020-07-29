var http = require('http');
var fs = require('fs');
var url = require('url');
var qs = require('querystring');
function templateHTML(path){
    fs.readFile(path,'utf-8',function(error,data){
        return data;
    });
}

var app = http.createServer(function(request,response){

    if(pathname == '/'){
         response.writeHead(200);
         response.end(templateHTML('./html/index.html'));
    }
})

app.listen(3000);