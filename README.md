# Play-Scrape
## A simple Play Store comments scraper written in Python
The aim of this project is to provide an easy yet functional module for scraping Google Play Store comments.
I use this personally for text mining projects that I'll publish later.

### Usage:
```
python play_scrape.py --pages <pages> --id <app_id> --output <outfile.json>
```
Where:
+ --pages are the number of pages to scrape, usually a page contains 40 reviews
+ --id is the app id, ex com.facebook.katana
+ --output is the name of the file where you want to store your results, default name is output.json

### Example:
```
python play_scrape.py  --pages 10 --id posteitaliane.posteapp.apppostepay --output poste.json

__________.__                   _________                                  
\______   \  | _____  ___.__.  /   _____/ ________________  ______   ____  
 |     ___/  | \__  \<   |  |  \_____  \_/ ___\_  __ \__  \ \____ \_/ __ \ 
 |    |   |  |__/ __ \___  |  /        \  \___|  | \// __ \|  |_> >  ___/ 
 |____|   |____(____  / ____| /_______  /\___  >__|  (____  /   __/ \___  >
                    \/\/              \/     \/           \/|__|        \/ 
                    Author Ancarani Riccardo
[*] Downloading the first 10 pages from: posteitaliane.posteapp.apppostepay
[*] Retrieved 40 reviews
[*] Retrieved 40 reviews
[*] Retrieved 40 reviews
[*] Retrieved 40 reviews
[*] Retrieved 40 reviews
[*] Retrieved 40 reviews
[*] Retrieved 40 reviews
[*] Retrieved 40 reviews
[*] Retrieved 40 reviews
[*] Retrieved 40 reviews
```

### Output:
The output is a JSON file with this structure:

```
{
  "results" : [ { "rating" : <rating>,
                  "review" : <review> } , ...
}
```

## Note:
This script currently only supports Italian comments, the generalization will be quite easy and I'll do it in the next future.
