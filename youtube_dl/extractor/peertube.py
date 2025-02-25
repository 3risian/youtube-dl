# coding: utf-8
from __future__ import unicode_literals

import re

from .common import InfoExtractor
from ..compat import compat_str
from ..utils import (
    int_or_none,
    parse_resolution,
    str_or_none,
    try_get,
    unified_timestamp,
    url_or_none,
    urljoin,
)


class PeerTubeIE(InfoExtractor):
    _INSTANCES_RE = r'''(?:
                            # Taken from https://instances.joinpeertube.org/instances
                            peertube\.rainbowswingers\.net|
                            tube\.stanisic\.nl|
                            peer\.suiri\.us|
                            medias\.libox\.fr|
                            videomensoif\.ynh\.fr|
                            peertube\.travelpandas\.eu|
                            peertube\.rachetjay\.fr|
                            peertube\.montecsys\.fr|
                            tube\.eskuero\.me|
                            peer\.tube|
                            peertube\.umeahackerspace\.se|
                            tube\.nx-pod\.de|
                            video\.monsieurbidouille\.fr|
                            tube\.openalgeria\.org|
                            vid\.lelux\.fi|
                            video\.anormallostpod\.ovh|
                            tube\.crapaud-fou\.org|
                            peertube\.stemy\.me|
                            lostpod\.space|
                            exode\.me|
                            peertube\.snargol\.com|
                            vis\.ion\.ovh|
                            videosdulib\.re|
                            v\.mbius\.io|
                            videos\.judrey\.eu|
                            peertube\.osureplayviewer\.xyz|
                            peertube\.mathieufamily\.ovh|
                            www\.videos-libr\.es|
                            fightforinfo\.com|
                            peertube\.fediverse\.ru|
                            peertube\.oiseauroch\.fr|
                            video\.nesven\.eu|
                            v\.bearvideo\.win|
                            video\.qoto\.org|
                            justporn\.cc|
                            video\.vny\.fr|
                            peervideo\.club|
                            tube\.taker\.fr|
                            peertube\.chantierlibre\.org|
                            tube\.ipfixe\.info|
                            tube\.kicou\.info|
                            tube\.dodsorf\.as|
                            videobit\.cc|
                            video\.yukari\.moe|
                            videos\.elbinario\.net|
                            hkvideo\.live|
                            pt\.tux\.tf|
                            www\.hkvideo\.live|
                            FIGHTFORINFO\.com|
                            pt\.765racing\.com|
                            peertube\.gnumeria\.eu\.org|
                            nordenmedia\.com|
                            peertube\.co\.uk|
                            tube\.darfweb\.eu|
                            tube\.kalah-france\.org|
                            0ch\.in|
                            vod\.mochi\.academy|
                            film\.node9\.org|
                            peertube\.hatthieves\.es|
                            video\.fitchfamily\.org|
                            peertube\.ddns\.net|
                            video\.ifuncle\.kr|
                            video\.fdlibre\.eu|
                            tube\.22decembre\.eu|
                            peertube\.harmoniescreatives\.com|
                            tube\.fabrigli\.fr|
                            video\.thedwyers\.co|
                            video\.bruitbruit\.com|
                            peertube\.foxfam\.club|
                            peer\.philoxweb\.be|
                            videos\.bugs\.social|
                            peertube\.malbert\.xyz|
                            peertube\.bilange\.ca|
                            libretube\.net|
                            diytelevision\.com|
                            peertube\.fedilab\.app|
                            libre\.video|
                            video\.mstddntfdn\.online|
                            us\.tv|
                            peertube\.sl-network\.fr|
                            peertube\.dynlinux\.io|
                            peertube\.david\.durieux\.family|
                            peertube\.linuxrocks\.online|
                            peerwatch\.xyz|
                            v\.kretschmann\.social|
                            tube\.otter\.sh|
                            yt\.is\.nota\.live|
                            tube\.dragonpsi\.xyz|
                            peertube\.boneheadmedia\.com|
                            videos\.funkwhale\.audio|
                            watch\.44con\.com|
                            peertube\.gcaillaut\.fr|
                            peertube\.icu|
                            pony\.tube|
                            spacepub\.space|
                            tube\.stbr\.io|
                            v\.mom-gay\.faith|
                            tube\.port0\.xyz|
                            peertube\.simounet\.net|
                            play\.jergefelt\.se|
                            peertube\.zeteo\.me|
                            tube\.danq\.me|
                            peertube\.kerenon\.com|
                            tube\.fab-l3\.org|
                            tube\.calculate\.social|
                            peertube\.mckillop\.org|
                            tube\.netzspielplatz\.de|
                            vod\.ksite\.de|
                            peertube\.laas\.fr|
                            tube\.govital\.net|
                            peertube\.stephenson\.cc|
                            bistule\.nohost\.me|
                            peertube\.kajalinifi\.de|
                            video\.ploud\.jp|
                            video\.omniatv\.com|
                            peertube\.ffs2play\.fr|
                            peertube\.leboulaire\.ovh|
                            peertube\.tronic-studio\.com|
                            peertube\.public\.cat|
                            peertube\.metalbanana\.net|
                            video\.1000i100\.fr|
                            peertube\.alter-nativ-voll\.de|
                            tube\.pasa\.tf|
                            tube\.worldofhauru\.xyz|
                            pt\.kamp\.site|
                            peertube\.teleassist\.fr|
                            videos\.mleduc\.xyz|
                            conf\.tube|
                            media\.privacyinternational\.org|
                            pt\.forty-two\.nl|
                            video\.halle-leaks\.de|
                            video\.grosskopfgames\.de|
                            peertube\.schaeferit\.de|
                            peertube\.jackbot\.fr|
                            tube\.extinctionrebellion\.fr|
                            peertube\.f-si\.org|
                            video\.subak\.ovh|
                            videos\.koweb\.fr|
                            peertube\.zergy\.net|
                            peertube\.roflcopter\.fr|
                            peertube\.floss-marketing-school\.com|
                            vloggers\.social|
                            peertube\.iriseden\.eu|
                            videos\.ubuntu-paris\.org|
                            peertube\.mastodon\.host|
                            armstube\.com|
                            peertube\.s2s\.video|
                            peertube\.lol|
                            tube\.open-plug\.eu|
                            open\.tube|
                            peertube\.ch|
                            peertube\.normandie-libre\.fr|
                            peertube\.slat\.org|
                            video\.lacaveatonton\.ovh|
                            peertube\.uno|
                            peertube\.servebeer\.com|
                            peertube\.fedi\.quebec|
                            tube\.h3z\.jp|
                            tube\.plus200\.com|
                            peertube\.eric\.ovh|
                            tube\.metadocs\.cc|
                            tube\.unmondemeilleur\.eu|
                            gouttedeau\.space|
                            video\.antirep\.net|
                            nrop\.cant\.at|
                            tube\.ksl-bmx\.de|
                            tube\.plaf\.fr|
                            tube\.tchncs\.de|
                            video\.devinberg\.com|
                            hitchtube\.fr|
                            peertube\.kosebamse\.com|
                            yunopeertube\.myddns\.me|
                            peertube\.varney\.fr|
                            peertube\.anon-kenkai\.com|
                            tube\.maiti\.info|
                            tubee\.fr|
                            videos\.dinofly\.com|
                            toobnix\.org|
                            videotape\.me|
                            voca\.tube|
                            video\.heromuster\.com|
                            video\.lemediatv\.fr|
                            video\.up\.edu\.ph|
                            balafon\.video|
                            video\.ivel\.fr|
                            thickrips\.cloud|
                            pt\.laurentkruger\.fr|
                            video\.monarch-pass\.net|
                            peertube\.artica\.center|
                            video\.alternanet\.fr|
                            indymotion\.fr|
                            fanvid\.stopthatimp\.net|
                            video\.farci\.org|
                            v\.lesterpig\.com|
                            video\.okaris\.de|
                            tube\.pawelko\.net|
                            peertube\.mablr\.org|
                            tube\.fede\.re|
                            pytu\.be|
                            evertron\.tv|
                            devtube\.dev-wiki\.de|
                            raptube\.antipub\.org|
                            video\.selea\.se|
                            peertube\.mygaia\.org|
                            video\.oh14\.de|
                            peertube\.livingutopia\.org|
                            peertube\.the-penguin\.de|
                            tube\.thechangebook\.org|
                            tube\.anjara\.eu|
                            pt\.pube\.tk|
                            video\.samedi\.pm|
                            mplayer\.demouliere\.eu|
                            widemus\.de|
                            peertube\.me|
                            peertube\.zapashcanon\.fr|
                            video\.latavernedejohnjohn\.fr|
                            peertube\.pcservice46\.fr|
                            peertube\.mazzonetto\.eu|
                            video\.irem\.univ-paris-diderot\.fr|
                            video\.livecchi\.cloud|
                            alttube\.fr|
                            video\.coop\.tools|
                            video\.cabane-libre\.org|
                            peertube\.openstreetmap\.fr|
                            videos\.alolise\.org|
                            irrsinn\.video|
                            video\.antopie\.org|
                            scitech\.video|
                            tube2\.nemsia\.org|
                            video\.amic37\.fr|
                            peertube\.freeforge\.eu|
                            video\.arbitrarion\.com|
                            video\.datsemultimedia\.com|
                            stoptrackingus\.tv|
                            peertube\.ricostrongxxx\.com|
                            docker\.videos\.lecygnenoir\.info|
                            peertube\.togart\.de|
                            tube\.postblue\.info|
                            videos\.domainepublic\.net|
                            peertube\.cyber-tribal\.com|
                            video\.gresille\.org|
                            peertube\.dsmouse\.net|
                            cinema\.yunohost\.support|
                            tube\.theocevaer\.fr|
                            repro\.video|
                            tube\.4aem\.com|
                            quaziinc\.com|
                            peertube\.metawurst\.space|
                            videos\.wakapo\.com|
                            video\.ploud\.fr|
                            video\.freeradical\.zone|
                            tube\.valinor\.fr|
                            refuznik\.video|
                            pt\.kircheneuenburg\.de|
                            peertube\.asrun\.eu|
                            peertube\.lagob\.fr|
                            videos\.side-ways\.net|
                            91video\.online|
                            video\.valme\.io|
                            video\.taboulisme\.com|
                            videos-libr\.es|
                            tv\.mooh\.fr|
                            nuage\.acostey\.fr|
                            video\.monsieur-a\.fr|
                            peertube\.librelois\.fr|
                            videos\.pair2jeux\.tube|
                            videos\.pueseso\.club|
                            peer\.mathdacloud\.ovh|
                            media\.assassinate-you\.net|
                            vidcommons\.org|
                            ptube\.rousset\.nom\.fr|
                            tube\.cyano\.at|
                            videos\.squat\.net|
                            video\.iphodase\.fr|
                            peertube\.makotoworkshop\.org|
                            peertube\.serveur\.slv-valbonne\.fr|
                            vault\.mle\.party|
                            hostyour\.tv|
                            videos\.hack2g2\.fr|
                            libre\.tube|
                            pire\.artisanlogiciel\.net|
                            videos\.numerique-en-commun\.fr|
                            video\.netsyms\.com|
                            video\.die-partei\.social|
                            video\.writeas\.org|
                            peertube\.swarm\.solvingmaz\.es|
                            tube\.pericoloso\.ovh|
                            watching\.cypherpunk\.observer|
                            videos\.adhocmusic\.com|
                            tube\.rfc1149\.net|
                            peertube\.librelabucm\.org|
                            videos\.numericoop\.fr|
                            peertube\.koehn\.com|
                            peertube\.anarchmusicall\.net|
                            tube\.kampftoast\.de|
                            vid\.y-y\.li|
                            peertube\.xtenz\.xyz|
                            diode\.zone|
                            tube\.egf\.mn|
                            peertube\.nomagic\.uk|
                            visionon\.tv|
                            videos\.koumoul\.com|
                            video\.rastapuls\.com|
                            video\.mantlepro\.com|
                            video\.deadsuperhero\.com|
                            peertube\.musicstudio\.pro|
                            peertube\.we-keys\.fr|
                            artitube\.artifaille\.fr|
                            peertube\.ethernia\.net|
                            tube\.midov\.pl|
                            peertube\.fr|
                            watch\.snoot\.tube|
                            peertube\.donnadieu\.fr|
                            argos\.aquilenet\.fr|
                            tube\.nemsia\.org|
                            tube\.bruniau\.net|
                            videos\.darckoune\.moe|
                            tube\.traydent\.info|
                            dev\.videos\.lecygnenoir\.info|
                            peertube\.nayya\.org|
                            peertube\.live|
                            peertube\.mofgao\.space|
                            video\.lequerrec\.eu|
                            peertube\.amicale\.net|
                            aperi\.tube|
                            tube\.ac-lyon\.fr|
                            video\.lw1\.at|
                            www\.yiny\.org|
                            videos\.pofilo\.fr|
                            tube\.lou\.lt|
                            choob\.h\.etbus\.ch|
                            tube\.hoga\.fr|
                            peertube\.heberge\.fr|
                            video\.obermui\.de|
                            videos\.cloudfrancois\.fr|
                            betamax\.video|
                            video\.typica\.us|
                            tube\.piweb\.be|
                            video\.blender\.org|
                            peertube\.cat|
                            tube\.kdy\.ch|
                            pe\.ertu\.be|
                            peertube\.social|
                            videos\.lescommuns\.org|
                            tv\.datamol\.org|
                            videonaute\.fr|
                            dialup\.express|
                            peertube\.nogafa\.org|
                            megatube\.lilomoino\.fr|
                            peertube\.tamanoir\.foucry\.net|
                            peertube\.devosi\.org|
                            peertube\.1312\.media|
                            tube\.bootlicker\.party|
                            skeptikon\.fr|
                            video\.blueline\.mg|
                            tube\.homecomputing\.fr|
                            tube\.ouahpiti\.info|
                            video\.tedomum\.net|
                            video\.g3l\.org|
                            fontube\.fr|
                            peertube\.gaialabs\.ch|
                            tube\.kher\.nl|
                            peertube\.qtg\.fr|
                            video\.migennes\.net|
                            tube\.p2p\.legal|
                            troll\.tv|
                            videos\.iut-orsay\.fr|
                            peertube\.solidev\.net|
                            videos\.cemea\.org|
                            video\.passageenseine\.fr|
                            videos\.festivalparminous\.org|
                            peertube\.touhoppai\.moe|
                            sikke\.fi|
                            peer\.hostux\.social|
                            share\.tube|
                            peertube\.walkingmountains\.fr|
                            videos\.benpro\.fr|
                            peertube\.parleur\.net|
                            peertube\.heraut\.eu|
                            tube\.aquilenet\.fr|
                            peertube\.gegeweb\.eu|
                            framatube\.org|
                            thinkerview\.video|
                            tube\.conferences-gesticulees\.net|
                            peertube\.datagueule\.tv|
                            video\.lqdn\.fr|
                            tube\.mochi\.academy|
                            media\.zat\.im|
                            video\.colibris-outilslibres\.org|
                            tube\.svnet\.fr|
                            peertube\.video|
                            peertube3\.cpy\.re|
                            peertube2\.cpy\.re|
                            videos\.tcit\.fr|
                            peertube\.cpy\.re
                        )'''
    _UUID_RE = r'[\da-fA-F]{8}-[\da-fA-F]{4}-[\da-fA-F]{4}-[\da-fA-F]{4}-[\da-fA-F]{12}'
    _VALID_URL = r'''(?x)
                    (?:
                        peertube:(?P<host>[^:]+):|
                        https?://(?P<host_2>%s)/(?:videos/(?:watch|embed)|api/v\d/videos)/
                    )
                    (?P<id>%s)
                    ''' % (_INSTANCES_RE, _UUID_RE)
    _TESTS = [{
        'url': 'https://framatube.org/videos/watch/9c9de5e8-0a1e-484a-b099-e80766180a6d',
        'md5': '9bed8c0137913e17b86334e5885aacff',
        'info_dict': {
            'id': '9c9de5e8-0a1e-484a-b099-e80766180a6d',
            'ext': 'mp4',
            'title': 'What is PeerTube?',
            'description': '**[Want to help to translate this video?](https://weblate.framasoft.org/projects/what-is-peertube-video/)**\r\n\r\n**Take back the control of your videos! [#JoinPeertube](https://joinpeertube.org)**\r\n*A decentralized video hosting network, based on free/libre software!*\r\n\r\n**Animation Produced by:** [LILA](https://libreart.info) - [ZeMarmot Team](https://film.zemarmot.net)\r\n*Directed by* Aryeom\r\n*Assistant* Jehan\r\n**Licence**: [CC-By-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)\r\n\r\n**Sponsored by** [Framasoft](https://framasoft.org)\r\n\r\n**Music**: [Red Step Forward](http://play.dogmazic.net/song.php?song_id=52491) - CC-By Ken Bushima\r\n\r\n**Movie Clip**: [Caminades 3: Llamigos](http://www.caminandes.com/) CC-By Blender Institute\r\n\r\n**Video sources**: https://gitlab.gnome.org/Jehan/what-is-peertube/',
            'thumbnail': r're:https?://.*\.(?:jpg|png)',
            'timestamp': 1538391166,
            'upload_date': '20181001',
            'uploader': 'Framasoft',
            'uploader_id': '3',
            'uploader_url': 'https://framatube.org/accounts/framasoft',
            'channel': 'Les vidéos de Framasoft',
            'channel_id': '2',
            'channel_url': 'https://framatube.org/video-channels/bf54d359-cfad-4935-9d45-9d6be93f63e8',
            'language': 'en',
            'license': 'Attribution - Share Alike',
            'duration': 113,
            'view_count': int,
            'like_count': int,
            'dislike_count': int,
            'tags': ['framasoft', 'peertube'],
            'categories': ['Science & Technology'],
        }
    }, {
        'url': 'https://peertube.tamanoir.foucry.net/videos/watch/0b04f13d-1e18-4f1d-814e-4979aa7c9c44',
        'only_matching': True,
    }, {
        # nsfw
        'url': 'https://tube.22decembre.eu/videos/watch/9bb88cd3-9959-46d9-9ab9-33d2bb704c39',
        'only_matching': True,
    }, {
        'url': 'https://tube.22decembre.eu/videos/embed/fed67262-6edb-4d1c-833b-daa9085c71d7',
        'only_matching': True,
    }, {
        'url': 'https://tube.openalgeria.org/api/v1/videos/c1875674-97d0-4c94-a058-3f7e64c962e8',
        'only_matching': True,
    }, {
        'url': 'peertube:video.blender.org:b37a5b9f-e6b5-415c-b700-04a5cd6ec205',
        'only_matching': True,
    }]

    @staticmethod
    def _extract_peertube_url(webpage, source_url):
        mobj = re.match(
            r'https?://(?P<host>[^/]+)/videos/(?:watch|embed)/(?P<id>%s)'
            % PeerTubeIE._UUID_RE, source_url)
        if mobj and any(p in webpage for p in (
                '<title>PeerTube<',
                'There will be other non JS-based clients to access PeerTube',
                '>We are sorry but it seems that PeerTube is not compatible with your web browser.<')):
            return 'peertube:%s:%s' % mobj.group('host', 'id')

    @staticmethod
    def _extract_urls(webpage, source_url):
        entries = re.findall(
            r'''(?x)<iframe[^>]+\bsrc=["\'](?P<url>(?:https?:)?//%s/videos/embed/%s)'''
            % (PeerTubeIE._INSTANCES_RE, PeerTubeIE._UUID_RE), webpage)
        if not entries:
            peertube_url = PeerTubeIE._extract_peertube_url(webpage, source_url)
            if peertube_url:
                entries = [peertube_url]
        return entries

    def _get_subtitles(self, host, video_id):
        video_captions = self._download_json(
            'https://%s/api/v1/videos/%s/captions' % (host, video_id), video_id, fatal=False)
        if not isinstance(video_captions, dict):
            return None

        subtitles = {}
        for entry in video_captions.get('data'):
            language_id = try_get(entry, lambda x: x['language']['id'], compat_str)
            caption_path = str_or_none(entry.get('captionPath'))
            if language_id and caption_path:
                caption_url = urljoin('https://%s' % host, entry.get('captionPath'))
                subtitles.setdefault(language_id, []).append({
                    'url': caption_url,
                })
        return subtitles

    def _real_extract(self, url):
        mobj = re.match(self._VALID_URL, url)
        host = mobj.group('host') or mobj.group('host_2')
        video_id = mobj.group('id')

        video = self._download_json(
            'https://%s/api/v1/videos/%s' % (host, video_id), video_id)

        title = video['name']

        formats = []
        for file_ in video['files']:
            if not isinstance(file_, dict):
                continue
            file_url = url_or_none(file_.get('fileUrl'))
            if not file_url:
                continue
            file_size = int_or_none(file_.get('size'))
            format_id = try_get(
                file_, lambda x: x['resolution']['label'], compat_str)
            f = parse_resolution(format_id)
            f.update({
                'url': file_url,
                'format_id': format_id,
                'filesize': file_size,
            })
            formats.append(f)
        self._sort_formats(formats)

        video_description = self._download_json(
            'https://%s/api/v1/videos/%s/description' % (host, video_id), video_id, fatal=False)

        description = None
        if isinstance(video_description, dict):
            description = str_or_none(video_description.get('description'))

        subtitles = self.extract_subtitles(host, video_id)

        def data(section, field, type_):
            return try_get(video, lambda x: x[section][field], type_)

        def account_data(field, type_):
            return data('account', field, type_)

        def channel_data(field, type_):
            return data('channel', field, type_)

        category = data('category', 'label', compat_str)
        categories = [category] if category else None

        nsfw = video.get('nsfw')
        if nsfw is bool:
            age_limit = 18 if nsfw else 0
        else:
            age_limit = None

        return {
            'id': video_id,
            'title': title,
            'description': description,
            'thumbnail': urljoin(url, video.get('thumbnailPath')),
            'timestamp': unified_timestamp(video.get('publishedAt')),
            'uploader': account_data('displayName', compat_str),
            'uploader_id': str(account_data('id', int)),
            'uploader_url': url_or_none(account_data('url', compat_str)),
            'channel': channel_data('displayName', compat_str),
            'channel_id': str(channel_data('id', int)),
            'channel_url': url_or_none(channel_data('url', compat_str)),
            'language': data('language', 'id', compat_str),
            'license': data('licence', 'label', compat_str),
            'duration': int_or_none(video.get('duration')),
            'view_count': int_or_none(video.get('views')),
            'like_count': int_or_none(video.get('likes')),
            'dislike_count': int_or_none(video.get('dislikes')),
            'age_limit': age_limit,
            'tags': try_get(video, lambda x: x['tags'], list),
            'categories': categories,
            'formats': formats,
            'subtitles': subtitles
        }
