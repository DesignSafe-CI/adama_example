from IPython.core.display import HTML, Javascript
from textwrap import dedent


def map_init():
    js = dedent(
        """
        window.gmap_initialize = function() {};
        $.getScript('https://maps.googleapis.com/maps/api/js?v=3&sensor=false&callback=gmap_initialize');
        """)
    return Javascript(data=js)

    
def map_display(data,
                token=None,
                display=True, 
                center_latitude=18.5333, 
                center_longitude=-72.3333, 
                zoom=9):

    div_id = "map"
    html = '<div id="{}" style="height: 600px;"/>'.format(div_id)
    marker_template = """
        var myLatlng = new google.maps.LatLng({lat},{lng});
        var marker_{i} = new google.maps.Marker({{ 
            position: myLatlng,
            map: map,
            title: "demo"
        }});
        var contentString = '';
        var infowindow_{i} = new google.maps.InfoWindow({{ 
            content: 'loading...'
        }});
        google.maps.event.addListener(marker_{i}, 'click', function() {{ 
            var xhr = new XMLHttpRequest();
            xhr.open('GET', 'https://api.araport.org/community/v0.3/walter-dev/haiti_images_v0.1/search?building={building}', true);
            xhr.responseType = 'blob';
            xhr.setRequestHeader('Authorization', 'Bearer {token}');

            xhr.onload = function(e) {{
                if (this.status == 200) {{
                    var blob = this.response;
                    var fr = new FileReader();
                    fr.onload = function() {{
                        var dataUrl = fr.result;
                        infowindow_{i}.setContent('<img src="' + dataUrl + '" width=300 />');
                    }};
                    fr.readAsDataURL(blob);
                }}
            }};
            xhr.send();
            infowindow_{i}.open(map, marker_{i});
            if (lastWindow) {{ 
                lastWindow.close();
                lastWindow = null;
            }} else {{
                lastWindow = infowindow_{i};
            }}
      }});
    """
    js_init = """
        <script type="text/Javascript">
            (function() {{
                var mapOptions = {{
                    zoom: {zoom},
                    center: new google.maps.LatLng({lat}, {lng})
                }};
                var map = new google.maps.Map(document.getElementById('{elt}'), mapOptions);
                var lastWindow = false;
                var transitLayer = new google.maps.TransitLayer();
                transitLayer.setMap(map);
        """.format(zoom=zoom, lat=center_latitude, lng=center_longitude, elt=div_id)
    js_end = """
            })();  
        </script>
    """
    markers = [marker_template.format(i=i, lat=lat, lng=lng, token=token, building=bldg) 
               for (i, (bldg, lat, lng)) in enumerate(data)]
    js_markers = ''.join(markers)
    html = html + js_init + js_markers + js_end
    return HTML(html)
