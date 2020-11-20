import flask
import re
import sys

import requests
from headers import headers
import urls
from flask import request
a = flask.Flask(__name__)

    
 
                      
@a.route('/')
def home():
    
    
    return "create By Infinitrocyber 👍👍👍"                           
@a.route("/zee")
def query():
            head = ' <!DOCTYPE html><html><head><meta charset="utf-8"><title>'
            heads= '</title><link rel="stylesheet" href="https://cdn.plyr.io/1.8.2/plyr.css"></head>'
            body = '<body><video preload="none" id="player" autoplay controls crossorigin></video><script src="https://cdn.plyr.io/1.8.2/plyr.js"></script><script src="https://cdn.jsdelivr.net/hls.js/latest/hls.js"></script>'
            script='<script>(function () {var video = document.querySelector("#player");if (Hls.isSupported()) {var hls = new Hls();hls.loadSource("'
            scripts=' ");hls.attachMedia(video);hls.on(Hls.Events.MANIFEST_PARSED,function() {video.play();});}plyr.setup(video);})();</script></body></html>'
            w = request.args.get('url')
            req1 = requests.get(urls.token_url1, headers=headers).json()
            rgx = re.findall("([0-9]?\w+)", w)[-3:]
            req2 = requests.get(urls.platform_token).json()["token"]
            headers["X-Access-Token"] = req2
            req3 = requests.get(urls.token_url2, headers=headers).json()
            if "zee" in w:
                r1 = requests.get(urls.search_api_endpoint + "-".join(rgx),
                                            headers=headers, 
                                            params={"translation":"en", "country":"IN"}).json()
                g1 = (r1["hls"][0].replace("drm", "hls") + req1["video_token"])
                return head+r1["title"]+heads+body+script+urls.stream_baseurl+g1+scripts
            else:
                return "no url or drm protected"
@a.route("/id")
def id():
            head = ' <!DOCTYPE html><html><head><meta charset="utf-8"><title>'
            heads= '</title><link rel="stylesheet" href="https://cdn.plyr.io/1.8.2/plyr.css"></head>'
            body = '<body><video preload="none" id="player" autoplay controls crossorigin></video><script src="https://cdn.plyr.io/1.8.2/plyr.js"></script><script src="https://cdn.jsdelivr.net/hls.js/latest/hls.js"></script>'
            script='<script>(function () {var video = document.querySelector("#player");if (Hls.isSupported()) {var hls = new Hls();hls.loadSource("'
            scripts=' ");hls.attachMedia(video);hls.on(Hls.Events.MANIFEST_PARSED,function() {video.play();});}plyr.setup(video);})();</script></body></html>'
            w = request.args.get('url')
            req1 = requests.get(urls.token_url1, headers=headers).json()
            #rgx = w
            req2 = requests.get(urls.platform_token).json()["token"]
            headers["X-Access-Token"] = req2
            req3 = requests.get(urls.token_url2, headers=headers).json()
           
            r1 = requests.get(urls.search_api_endpoint + w,headers=headers, params={"translation":"en", "country":"IN"}).json()
            g1 = (r1["hls"][0].replace("drm", "hls") + req1["video_token"])
            return head+r1["title"]+heads+body+script+urls.stream_baseurl+g1+scripts
  

 
                 
                

a.run("127.0.0.1", 8080, debug=False)

