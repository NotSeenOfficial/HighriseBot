import json
from highrise import BaseBot, User
import asyncio
from asyncio import Task
from owner import OWNER_USER


class LoopEmote:

    @staticmethod
    def load_UserEmote_ids(file_path="UserEmotes.json"):
        try:
            with open(file_path, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    @staticmethod
    def save_UserEmote_ids(UserEmote_ids, file_path="UserEmotes.json"):
        with open(file_path, "w") as f:
            json.dump(UserEmote_ids, f)

            
    def __init__(self, bot: BaseBot):
        self.bot = bot
        self.emote_list: list[tuple[int, str, str]] = [
    (0, 'jetpack', 'hcc-jetpack'),
    (1, 'fairyfloat', 'idle-floating'),
    (2, 'fairytwirl', 'emote-looping'),
    (3, 'smooch', 'emote-kissing-bound'),
    (4, 'launch', 'emote-launch'),
    (5, 'float', 'emote-float'),
    (6, 'lust', 'emote-lust'),
    (7, 'creepypuppet', 'dance-creepypuppet'),
    (8, 'repose', 'sit-relaxed'),
    (9, 'enthused', 'idle-enthusiastic'),
    (10, 'anime', 'dance-anime'),
    (11, 'gravity', 'emote-gravity'),
    (12, 'toilet', 'idle-toilet'),
    (13, 'astro', 'emote-astronaut'),
    (14, 'flex', 'emoji-flex'),
    (15, 'timejump', 'emote-timejump'),
    (16, 'penguin', 'dance-pinguin'),
    (17, 'kawaii', 'dance-kawai'),
    (18, 'jinglebell', 'dance-jinglebell'),
    (19, 'skating', 'emote-iceskating'),
    (20, 'teleporting', 'emote-teleporting'),
    (21, 'energyball', 'emote-energyball'),
    (22, 'pushit', 'dance-employee'),
    (23, 'boxer', 'emote-boxer'),
    (24, 'creepycute', 'emote-creepycute'),
    (25, 'headblow', 'emote-headblowup'),
    (26, 'wrong', 'dance-wrong'),
    (27, 'weirdd', 'dance-weird'),
    (28, 'uwu', 'idle-uwu'),
    (29, 'snake', 'emote-snake'),
    (30, 'singing', 'idle_singing'),
    (31, 'model', 'emote-model'),
    (32, 'maniac', 'emote-maniac'),
    (33, 'snow', 'emote-snowangel'),
    (34, 'ride', 'emote-sleigh'),
    (35, 'icecream', 'dance-icecream'),
    (36, 'surprise', 'emote-pose6'),
    (37, 'touch', 'dance-touch'),
    (38, 'swordfight', 'emote-swordfight'),
    (39, 'airguitar', 'idle-guitar'),
    (40, 'zombie', 'emote-zombierun'),
    (41, 'fashion', 'emote-fashionista'),
    (42, 'curtsy', 'emote-curtsy'),
    (43, 'cutee', 'emote-cute'),
    (44, 'telek', 'emote-telekinesis'),
    (45, 'russian', 'dance-russian'),
    (46, 'blackpink', 'dance-blackpink'),
    (47, 'shopping', 'dance-shoppingcart'),
    (48, 'tiktok6', 'dance-tiktok11'),
    (49, 'tiktok5', 'dance-tiktok9'),
    (50, 'tiktok4', 'dance-tiktok8'),
    (51, 'tiktok3', 'idle-dance-tiktok4'),
    (52, 'tiktok2', 'dance-tiktok2'),
    (53, 'tiktok1', 'dance-tiktok10'),
    (54, 'hott', 'emote-hot'),
    (55, 'charge', 'emote-charging'),
    (56, 'greedy', 'emote-greedy'),
    (57, 'confused', 'emote-confused'),
    (58, 'punkguitar', 'emote-punkguitar'),
    (59, 'shy', 'emote-shy2'),
    (60, 'wildd', 'idle-wild'),
    (61, 'nervous', 'idle-nervous'),
    (62, 'hyped', 'emote-hyped'),
    (63, 'fishing', 'fishing-idle'),
    (64, 'frog', 'emote-frog'),
    (65, 'siu', 'emote-celebrationstep'),
    (66, 'snowballfight', 'emote-snowball'),
    (67, 'bow', 'emote-bow'),
    (68, 'thewave', 'emote-wave'),
    (69, 'tiredd', 'emote-tired'),
    (70, 'pennywise', 'dance-pennywise'),
    (71, 'superpose', 'emote-superpose'),  
    (72, 'pose8', 'emote-pose8'),
    (73, 'laugh', 'emote-laughing'),
    (74, 'kiss', 'emote-kiss'),
    (75, 'hellos', 'emote-hello'),
    (76, 'gift', 'emote-gift'),
    (77, 'pose10', 'emote-pose10'),
    (78, 'thumbsup', 'emoji-thumbsup'),
    (79, 'cursing', 'emoji-cursing'),
    (80, 'celebrate', 'emoji-celebrate'),
    (81, 'macarena', 'dance-macarena'),
    (82, 'sitt', 'idle-loop-sitfloor'),
    (83, 'gag', 'emoji-gagging'),          
    (84, 'superpose', 'emote-superpose'),
    (85, 'pose7', 'emote-pose7'),
    (86, 'deny', 'emote-no'),
    (87, 'casual', 'idle-dance-casual'),   
    (88, 'pose1', 'emote-pose1'),
    (89, 'pose3', 'emote-pose3'),
    (90, 'pose5', 'emote-pose5'),
    (91, 'cutey', 'emote-cutey'),
    (92, 'thatsright', 'emote-yes'),
    (93, 'pose9', 'emote-pose9'),
    (94, 'angryy', 'emoji-angry'),   
    (95, 'miningmine', 'mining-mine'),
    (96, 'miningsuccess', 'mining-success'),
    (97, 'fishingpull', 'fishing-pull'),
    (98, 'fishingpullsmall', 'fishing-pull-small'),
    (99, 'fishingcast', 'fishing-cast'),
    (100, 'rest', 'idle-rest-bound'),
    
    (101, 'gwiddy', 'dance-griddy'),
    (102, 'electrified', 'emote-electrified'),
    (103, 'twitch', 'emote-twitched'),
    (104, 'handwalk', 'emote-handwalk'),
    (105, 'kid', 'dance-kid'),
    (106, 'hero', 'idle-hero'),    
    (107, 'space', 'idle-space'), 
    (108, 'tiktok5', 'dance-tiktok5'),  
    (109, 'fading', 'emote-fading'),  
    (110, 'dinner', 'emote-dinner'),  
    (111, 'opera', 'emote-opera'),  
    (112, 'hiphopdance', 'dance-hiphop'),  
    (113, 'tiktok15', 'dance-tiktok15'),  
    (114, 'tiktok6', 'dance-tiktok6'),  
    (115, 'juggling', 'emote-juggling'),  
    (116, 'thief', 'emote-thief'),  
    (117, 'sheephop', 'emote-sheephop'),  
    (118, 'shocked', 'emote-shocked'),  
    (119, 'flirt', 'emote-flirt'),  
    (120, 'gooey', 'emote-gooey'),  
    (121, 'outfit2', 'emote-outfit2'),  
    (122, 'fireworks', 'emote-fireworks'),  
    (123, 'tiktok7', 'dance-tiktok7'),  
    (124, 'doomscroll', 'emote-phone'),  
    (125, 'yapping', 'idle-phone'),  
    (126, 'selfietime', 'idle-phone-camera'),  
    (127, 'knockknock', 'emote-knocking-screen'),  
    (128, 'oops', 'emote-oops'),  
    (129, 'wavey', 'emote-wavey'),  
    (130, 'cold', 'idle-cold'),  
    (131, 'surf', 'emote-surf'),  
    (132, 'tacticalflex', 'emote-rifle'),  
    (133, 'pose11', 'emote-pose11'),  
    (134, 'runhop', 'emote-runhop'),  
    (135, 'outfit', 'emote-outfit'),  
    (136, 'pose12', 'emote-pose12'),  
    (137, 'twerkit', 'dance-twerk'),  
    (138, 'pokedance', 'dance-tiktok12'),  
    (139, 'stargazer', 'emote-stargazer'),  
    (140, 'hopscotch', 'emote-hopscotch'),  
    (141, 'receivedisappointed', 'emote-receive-disappointed'),  
    (142, 'receivehappy', 'emote-receive-happy'),  
    (143, 'tiktok3', 'dance-tiktok3'),  
    (144, 'tiktok1', 'dance-tiktok1'),  
    (145, 'tiktok62', 'idle-dance-tiktok6'),  
    (146, 'grrr', 'emote-pose2'),  
    (147, 'shuffle', 'dance-shuffle'),  
    (148, 'musclepose', 'emote-pose4'),  
    (149, 'anime3', 'dance-anime3'),  
    (150, 'donttouch', 'dance-tiktok13'),  
    (151, 'runn', 'run-vertical'),  
    (152, 'headless', 'idle-headless'),  
    (153, 'uhmmm', 'emote-thought'),  
    (154, 'passionatekiss', 'emote-kissing-passionate'),  
    (155, 'tiktok16', 'emote-outfit2'),  
    (156, 'breakscreen', 'profile-breakscreen'),  
    (157, 'shush', 'emoji-shush'),
    (158, 'armcannon', 'emote-armcannon'),
    (159, 'crouch', 'idle-crouched'),
    (160, 'laidback', 'sit-open'),
    (161, 'handaintheair', 'dance-handsup'),
    (162, 'ghostfloat', 'emote-ghost-idle'),
    (163, 'relaxed', 'idle_layingdown2'),
    (164, 'attentive', 'idle_layingdown'),
    (165, 'tap loop', 'idle-loop-tapdance'),
    (166, 'posh', 'idle-posh'),
    (167, 'shrink', 'emote-shrink'),
    (168, 'rest', 'sit-idle-cute'),
    (169, 'zombie', 'idle_zombie'),
    (170, 'relaxed', 'idle_layingdown2'),
    (171, 'attentive', 'idle_layingdown'),
    (172, 'sleepy', 'idle-sleep'),
    (173, 'pouty', 'idle-sad'),
    (174, 'posh', 'idle-posh'),
    (175, 'tired', 'idle-loop-tired'),
    (176, 'taploop', 'idle-loop-tapdance'),
    (177, 'shy2', 'idle-loop-shy'),
    (178, 'bummed', 'idle-loop-sad'),
    (179, 'chillin', 'idle-loop-happy'),
    (180, 'annoyed', 'idle-loop-annoyed'),
    (181, 'aerobics', 'idle-loop-aerobics'),
    (182, 'ponder', 'idle-lookup'),
    (183, 'heropose', 'idle-hero'),
    (184, 'relaxing', 'idle-floorsleeping2'),
    (185, 'cozynap', 'idle-floorsleeping'),
    (186, 'boogieswing', 'idle-dance-swinging'),
    (187, 'feelbeat', 'idle-dance-headbobbing'),
    (188, 'irritated', 'idle-angry'),
    (189, 'ibelieve', 'emote-wings'),
    (190, 'think', 'emote-think'),
    (191, 'theatrical', 'emote-theatrical'),
    (192, 'tapdance', 'emote-tapdance'),
    (193, 'superrun', 'emote-superrun'),
    (194, 'superpunch', 'emote-superpunch'),
    (195, 'sumo', 'emote-sumo'),
    (196, 'thumbsuck', 'emote-suckthumb'),
    (197, 'splits', 'emote-splitsdrop'),
    (198, 'secretshake', 'emote-secrethandshake'),
    (199, 'ropepull', 'emote-ropepull'),
    (200, 'roll', 'emote-roll'),
    (201, 'rofl', 'emote-rofl'),
    (202, 'robotdance', 'emote-robot'),
    (203, 'rainbow', 'emote-rainbow'),
    (204, 'propose', 'emote-proposing'),
    (205, 'peekaboo', 'emote-peekaboo'),
    (206, 'peace', 'emote-peace'),
    (207, 'panic', 'emote-panic'),
    (208, 'ninjarun', 'emote-ninjarun'),
    (209, 'nightfever', 'emote-nightfever'),
    (210, 'monsterfail', 'emote-monster_fail'),
    (211, 'levelup', 'emote-levelup'),
    (212, 'amused', 'emote-laughing2'),
    (213, 'superkick', 'emote-kicking'),
    (214, 'jump', 'emote-jumpb'),
    (215, 'judochop', 'emote-judochop'),
    (216, 'jetpackfly', 'emote-jetpack'),
    (217, 'hugyourself', 'emote-hugyourself'),
    (218, 'heroentrance', 'emote-hero'),
    (219, 'headball', 'emote-headball'),
    (220, 'harlemshake', 'emote-harlemshake'),
    (221, 'happyy', 'emote-happy'),
    (222, 'handstand', 'emote-handstand'),
    (223, 'graceful', 'emote-graceful'),
    (224, 'moonwalk', 'emote-gordonshuffle'),
    (225, 'ghostfloat', 'emote-ghost-idle'),
    (226, 'gangnam', 'emote-gangnam'),
    (227, 'frolic', 'emote-frollicking'),
    (228, 'faint', 'emote-fainting'),
    (229, 'clumsy', 'emote-fail2'),
    (230, 'fall', 'emote-fail1'),
    (231, 'exasperated', 'emote-exasperated'),
    (232, 'elbowbump', 'emote-elbowbump'),
    (233, 'disco', 'emote-disco'),
    (234, 'blastoff', 'emote-disappear'),
    (235, 'faintdrop', 'emote-deathdrop'),
    (236, 'collapse', 'emote-death2'),
    (237, 'revival', 'emote-death'),
    (238, 'dab', 'emote-dab'),
    (239, 'cold', 'emote-cold'),
    (240, 'bunnyhop', 'emote-bunnyhop'),
    (241, 'boo', 'emote-boo'),
    (242, 'homerun', 'emote-baseball'),
    (243, 'apart', 'emote-apart'),
    (244, 'point', 'emoji-there'),
    (245, 'sneeze', 'emoji-sneeze'),
    (246, 'smirk', 'emoji-smirking'),
    (247, 'sick', 'emoji-sick'),
    (248, 'gasp', 'emoji-scared'),
    (249, 'punch', 'emoji-punch'),
    (250, 'pray', 'emoji-pray'),
    (251, 'stinky', 'emoji-poop'),
    (252, 'naughty', 'emoji-naughty'),
    (253, 'mindblown', 'emoji-mind-blown'),
    (254, 'lying', 'emoji-lying'),
    (255, 'levitate', 'emoji-halo'),
    (256, 'firelunge', 'emoji-hadoken'),
    (257, 'giveup', 'emoji-give-up'),
    (258, 'stunned', 'emoji-dizzy'),
    (259, 'clap', 'emoji-clapping'),
    (260, 'arrogance', 'emoji-arrogance'),
    (261, 'voguehands', 'dance-voguehands'),
    (262, 'yogaflow', 'dance-spiritual'),
    (263, 'smoothwalk', 'dance-smoothwalk'),
    (264, 'ringonit', 'dance-singleladies'),
    (265, 'roboticdance', 'dance-robotic'),
    (266, 'orangejuice', 'dance-orangejustice'),
    (267, 'rockout', 'dance-metal'),
    (268, 'karate', 'dance-martial-artist'),
    (269, 'handsinair', 'dance-handsup'),
    (270, 'floss', 'dance-floss'),
    (271, 'duckwalk', 'dance-duckwalk'),
    (272, 'breakdance', 'dance-breakdance'),
    (273, 'pushups', 'dance-aerobics'),
    (274, 'salutee', 'emote-attention'),
    (275, 'ghost', 'emoji-ghost'),
    (276, 'heartshape', 'emote-heartshape'),
    (277, 'hug', 'emote-hug'),
    (278, 'laugh2', 'emote-lagughing'),
    (279, 'eyeroll', 'emoji-eyeroll'),
    (280, 'embarrassed', 'emote-embarrassed'),
    (281, 'sexydance', 'dance-sexy'),
    (282, 'puppet', 'emote-puppet'),
    (283, 'fightidle', 'idle-fighter'),
    (284, 'zombierun2', 'emote-zombierun'),
    (285, 'frustrated', 'emote-frustrated'),
    (286, 'stargazing', 'emote-stargaze'),
    (287, 'slap', 'emote-slap'),
    (288, 'kawaiigogo', 'emote-kawaiigogo'),
    (289, 'tiktok7', 'idle-dance-tiktok7'),
    (290, 'shrink', 'emote-shrink'),
    (291, 'facepalm', 'emote-exasperatedb'),
    (292, 'hearteyes', 'emote-hearteyes'),
    (293, 'heartfingers', 'emote-heartfingers'),
    (294, 'trampoline', 'emote-trampoline'),
    (295, 'howl1', 'emote-howl'),
    (296, 'howl2', 'idle-howl'),
    (297, 'phone1', 'idle-laying-phone-texting'),
    (298, 'phone2', 'idle-laying-phone-talking'),
    (299, 'kawaiigogo', 'emote-kawaiigogo'),
    (300, 'stargazing', 'emote-stargaze'),
    (301, 'gift', 'emote-gift'),
    (302, 'zombie dance', 'dance-zombie'),
    (303, 'vogue hands', 'dance-voguehands'),
    (304, 'stinky', 'emoji-poop'),
    (305, 'ghost', 'emoji-ghost'),
    (306, 'Levitate', 'emoji-halo'),
    (307, 'Prince', 'dance-freshprince'),
    (308, 'Sick', 'emoji-sick'),
    (309, 'Pray', 'emoji-pray'),
    (310, 'Gasp', 'emoji-scared')
]
        self.emote_durations = {
            'flex': 2.099351,
            'jetpack': 25.5,
            'toilet': 32.174447,
            'frog': 14.55257,
            'float': 8.995302,
            'enthused': 15.941537,
            'gravity': 8.955966,
            'russian': 10.252905,
            'zombie': 12.922772,
            'punkguitar': 9.365807,
            'airguitar': 13.229398,
            'teleporting': 11.7676,
            'charge': 8.025079,
            'hott': 4.353037,
            'tiktok1': 8.225648,
            'tiktok2': 10.392353,
            'tiktok3': 15.500708,
            'tiktok4': 10.938702,
            'tiktok5': 11.892918,
            'shopping': 4.316035,
            'blackpink': 7.150958,
            'anime': 8.46671,
            'telek': 10.492032,
            'cutee': 3.26032,
            'curtsy': 2.425714,
            'fashion': 5.606485,
            'shy': 4.989278,
            'confused': 8.578827,
            'energyball': 7.575354,
            'gag': 5.500202,
            'icecream': 14.769573,
            'lust': 4.655965,
            'snow': 6.218627,
            'maniac': 4.906886,
            'model': 6.490173,
            'singing': 10.260182,
            'snake': 5.262578,
            'uwu': 24.761968,
            'weirdd': 21.556237,
            'wrong': 12.422389,
            'headblow': 11.667537,
            'creepycute': 7.902453,
            'boxer': 5.555702,
            'pushit': 8,
            'siu': 3.353703,
            'surprise': 5.375124,
            'skating': 7.299156,
            'wildd': 26.422824,
            'kawaii': 10.290789,
            'penguin': 11.58291,
            'timejump': 4.007305,
            'swordfight': 5.914365,
            'astro': 13.791175,
            'nervous': 21.714221,
            'jinglebell': 10.958832,
            'hyped': 7.492423,
            'repose': 29.3,
            'fairyfloat': 26,
            'fairytwirl': 9.0,
            'creepypuppet': 6.416121,
            'ride': 11.333165,
            'fishing': 16,
            'smooch': 6,
            'launch': 9.4,
            'tiktok6': 10.8,
            'sitt': 22.321055,
            'thatsright': 2.565001,
            'thewave': 2.690873,
            'tiredd': 4.61063,
            'snowballfight': 5.230467,
            'snowangel': 6.218627,
            'sad': 5.411073,
            'deny': 2.703034,
            'laugh': 2.69161,
            'kiss': 2.387175,
            'hellos': 2.734844,
            'exasperatedb': 2.722748,
            'bow': 3.344036,
            'thumbsup': 2.702369,
            'cursing': 2.382069,
            'celebrate': 3.412258,
            'angryy': 5.760023,
            'savage': 10.938702,
            'dontstartnow': 10.392353,
            'pennywise': 1.214349,
            'macarena': 12.214141,
            'hearteyes': 4.034386,
            'superpose': 4.530791,
            'pose7': 4.655283,
            'pose8': 4.808806,
            'casual': 9.079756,
            'pose1': 2.825795,
            'pose3': 5.10562,
            'pose5': 4.621532,
            'cutey': 3.26032,
            'pose10': 3.989871,
            'pose9': 4.583117,
            'gift': 5.8,
            'touch': 11.7,
            'miningmine': 3,
            'miningsuccess': 2.5,
            'fishingpull': 1,
            'fishingpullsmall': 1,
            'fishingcast': 1.5,
            'rest': 17.062613,
            'zombie': 28.754937,
            'relaxed': 21.546653,
            'attentive': 24.585168,
            'sleepy': 22.620446,
            'pouty': 24.377214,
            'posh': 21.851256,
            'tired': 21.959007,
            'taploop': 6.261593,
            'shy2': 16.47449,
            'bummed': 6.052999,
            'chillin': 18.798322,
            'annoyed': 17.058522,
            'aerobics': 8.507535,
            'ponder': 22.339865,
            'heropose': 21.877099,
            'relaxing': 17.253372,
            'cozynap': 13.935264,
            'boogieswing': 13.198551,
            'feelbeat': 25.367458,
            'irritated': 25.427848,
            'ibelieve': 13.134487,
            'think': 3.691104,
            'theatrical': 8.591869,
            'tapdance': 11.057294,
            'superrun': 6.273226,
            'superpunch': 3.751054,
            'sumo': 10.868834,
            'thumbsuck': 4.185944,
            'splits': 4.46931,
            'secretshake': 3.879024,
            'ropepull': 8.769656,
            'roll': 3.560517,
            'rofl': 6.314731,
            'robotdance': 7.607362,
            'rainbow': 2.813373,
            'propose': 4.27888,
            'peekaboo': 3.629867,
            'peace': 5.755004,
            'panic': 2.850966,
            'ninjarun': 4.754721,
            'nightfever': 5.488424,
            'monsterfail': 4.632708,
            'levelup': 6.0545,
            'amused': 5.056641,
            'superkick': 4.867992,
            'jump': 3.584234,
            'judochop': 2.427442,
            'jetpackfly': 16.759457,
            'hugyourself': 4.992751,
            'heroentrance': 4.996096,
            'headball': 10.073119,
            'harlemshake': 13.558597,
            'happyy': 3.483462,
            'handstand': 4.015678,
            'graceful': 3.7498,
            'moonwalk': 8.052307,
            'ghostfloat': 19.570492,
            'gangnam': 7.275486,
            'frolic': 3.700665,
            'faint': 18.423499,
            'clumsy': 6.475972,
            'fall': 5.617942,
            'exasperated': 2.367483,
            'elbowbump': 3.799768,
            'disco': 5.366973,
            'blastoff': 6.195985,
            'faintdrop': 3.762728,
            'collapse': 4.855549,
            'revival': 6.615967,
            'dab': 2.717871,
            'cold': 3.664348,
            'bunnyhop': 12.380685,
            'boo': 4.501502,
            'homerun': 7.254841,
            'apart': 4.809542,
            'point': 2.059095,
            'sneeze': 2.996694,
            'smirk': 4.823158,
            'sick': 5.070367,
            'gasp': 3.008487,
            'punch': 1.755783,
            'pray': 4.503179,
            'stinky': 4.795735,
            'naughty': 4.277602,
            'mindblown': 2.397167,
            'lying': 6.313748,
            'levitate': 5.837754,
            'firelunge': 2.723709,
            'giveup': 5.407888,
            'stunned': 4.053049,
            'clap': 2.161757,
            'arrogance': 6.869441,
            'voguehands': 9.150634,
            'yogaflow': 15.795092,
            'smoothwalk': 6.690023,
            'ringonit': 21.191372,
            'roboticdance': 17.814959,
            'orangejuice': 6.475263,
            'rockout': 15.076377,
            'karate': 13.284405,
            'handsinair': 22.283413,
            'floss': 21.329661,
            'duckwalk': 11.748784,
            'breakdance': 17.623849,
            'pushups': 8.796402,
            'salutee': 4.401206,
            'ghost': 3.472759,
            'heartshape': 6.232394,
            'hug': 3.503262,
            'laugh2': 1.125537,
            'eyeroll': 3.020264,
            'embarrassed': 7.414283,
            'sexydance': 12.30883,
            'puppet': 16.325823,
            'fightidle': 17.19123,
            'zombierun2': 9.182984,
            'frustrated': 5.584622,
            'stargazing': 1.127464,
            'slap': 2.724945,
            'kawaiigogo': 10,
            'tiktok7': 12.956484,
            'shrink': 8.738784,
            'facepalm': 2.722748,
            'hearteyes': 4.034386,
            'heartfingers': 4.001974,
            'trampoline': 15,
            'howl1': 10,
            'howl2': 10
        }  # Mapping emotes to their specific durations (in seconds)


    async def handle_command(self, user: User, message: str) -> None:
        UserEmote_ids = self.load_UserEmote_ids()
        
        if message.lower().startswith("!stoploopall"):
            if user.username.lower() not in OWNER_USER:
                await self.bot.highrise.send_whisper(user.id, "Vous n'avez pas la permission pour utiliser cette commande.")
                return
            taskgroup = self.bot.highrise.tg
            task_list: list[Task] = list(taskgroup._tasks)
            for task in task_list:
                if task.get_name().startswith("loop_all_"):
                    task.cancel()
            await self.bot.highrise.chat("Stopped all looping emotes!")
            return

        if message.lower().startswith("!loop all "):
            if user.username.lower() not in OWNER_USER:
                await self.bot.highrise.send_whisper(user.id, "Vous n'avez pas la permission pour utiliser cette commande.")
                return
            emote_query = message[10:].strip()
            emote_id = ""
            emote_name = ""

            if emote_query.isdigit():
                emote_number = int(emote_query)
                for emote in self.emote_list:
                    if emote[0] == emote_number:
                        emote_id = emote[2]
                        emote_name = emote[1]
                        break
            else:
                for emote in self.emote_list:
                    if emote[1].lower() == emote_query.lower():
                        emote_id = emote[2]
                        emote_name = emote[1]
                        break

            if not emote_id:
                await self.bot.highrise.send_whisper(user.id, "Invalid emote")
                return

            async def loop_all_emotes():
                while True:
                    try:
                        room_users = (await self.bot.highrise.get_room_users()).content
                        emote_tasks = []
                        for room_user, _ in room_users:
                            emote_tasks.append(self.bot.highrise.send_emote(emote_id, room_user.id))
                        if emote_tasks:
                            await asyncio.gather(*emote_tasks)
                        await asyncio.sleep(self.emote_durations.get(emote_name.lower(), 10))
                    except Exception as e:
                        print(f"Error in loop_all_emotes: {e}")
                        return

            taskgroup = self.bot.highrise.tg
            task = taskgroup.create_task(coro=loop_all_emotes())
            task.set_name(f"loop_all_{emote_name}")
            await self.bot.highrise.chat(f"Started looping emote [{emote_name}] for all users! Use !stoploopall to stop.")
            return

        if message.lower().endswith("all"):
            if len(message) < 4:
                return
            command = message[:-3].strip()
            if command.isdigit():
                emote_number = int(command)
                if emote_number in range(len(self.emote_list)):
                    emote_action = self.emote_list[emote_number][2]
            else:
                emote_action = None
                for emote in self.emote_list:
                    if emote[1].lower() == command.lower():
                        emote_action = emote[2]
                        break
            if emote_action:
                privilege_response = await self.bot.highrise.get_room_privilege(user.id)
                if not (privilege_response.moderator or user.username.lower() in OWNER_USER):
                    await self.bot.highrise.send_whisper(user.id, "Vous n'avez pas la permission pour utiliser cette commande.")
                    return
                try:
                    roomUsers = (await self.bot.highrise.get_room_users()).content
                    emote_tasks = []
                    for roomUser in roomUsers:
                        user_object = roomUser[0]
                        emote_tasks.append(self.bot.highrise.send_emote(emote_action, user_object.id))
                    if emote_tasks:
                        await asyncio.gather(*emote_tasks)
                except Exception as e:
                    logging.error(f"An error occurred in handle_command: {e}")
        
        # Check if message format is "!dual @username emotename" or "!dual @username emotenumber"
        if message.lower().startswith("!dual "):
            parts = message[6:].split()  # Split after "!dual "
            if len(parts) == 2 and parts[0].startswith("@"):
                target_username = parts[0][1:]  # Remove @ symbol
                emote_query = parts[1]
                
                # Check permissions
                if user.username.lower() not in OWNER_USER:
                    await self.bot.highrise.send_whisper(user.id, "Vous n'avez pas la permission pour utiliser cette commande.")
                    return

                # Find the emote (by number or name)
                emote_id = None
                emote_name = None
                if emote_query.isdigit():
                    emote_number = int(emote_query)
                    for emote in self.emote_list:
                        if emote[0] == emote_number:
                            emote_id = emote[2]
                            emote_name = emote[1]
                            break
                else:
                    for emote in self.emote_list:
                        if emote[1].lower() == emote_query.lower():
                            emote_id = emote[2]
                            emote_name = emote[1]
                            break

                if emote_id:
                    # Get room users and find target user
                    room_users = (await self.bot.highrise.get_room_users()).content
                    target_user_id = None
                    for room_user, _ in room_users:
                        if room_user.username.lower() == target_username.lower():
                            target_user_id = room_user.id
                            target_username = room_user.username  # Store original username casing
                            break
                    
                    if target_user_id:
                        # Make both users perform the emote
                        await self.bot.highrise.send_emote(emote_id, target_user_id)
                        await self.bot.highrise.send_emote(emote_id, user.id)
                        await self.bot.highrise.send_whisper(user.id, f"You and {target_username} performed emote [{emote_name}]")
                        return
                    else:
                        await self.bot.highrise.send_whisper(user.id, f"User {target_username} not found in room")
                        return
                else:
                    await self.bot.highrise.send_whisper(user.id, f"Invalid emote: {emote_query}")
                    return

        # Check if message is "!random @username"
        if message.lower().startswith("!random @"):
            target_username = message[8:].strip()  # Get username after @
            
            # Check permissions
            if user.username.lower() not in OWNER_USER:
                await self.bot.highrise.send_whisper(user.id, "Vous n'avez pas la permission pour utiliser cette commande.")
                return

            # Get room users and find target user
            room_users = (await self.bot.highrise.get_room_users()).content
            target_user_id = None
            for room_user, _ in room_users:
                if room_user.username.lower() == target_username.lower():
                    target_user_id = room_user.id
                    target_username = room_user.username  # Store original username casing
                    break
            
            if not target_user_id:
                await self.bot.highrise.send_whisper(user.id, f"User {target_username} not found in room")
                return

            async def random_emote_loop():
                while True:
                    try:
                        # Pick random emote
                        random_emote = random.choice(self.emote_list)
                        emote_id = random_emote[2]
                        emote_name = random_emote[1]
                        
                        # Send emote
                        await self.bot.highrise.send_emote(emote_id, target_user_id)
                        
                        # Wait for emote duration
                        sleep_duration = self.emote_durations.get(emote_name.lower(), 10)
                        await asyncio.sleep(sleep_duration)
                    except Exception as e:
                        print(f"Error in random emote loop: {e}")
                        return

            # Start random emote loop
            taskgroup = self.bot.highrise.tg
            task = taskgroup.create_task(coro=random_emote_loop())
            task.set_name(f"random_{target_username}")
            await self.bot.highrise.chat(f"Started random emotes for {target_username}! Use !stoprandom @{target_username} to stop.")
            return

        # Check if message is "!stoprandom @username" 
        if message.lower().startswith("!stoprandom @"):
            if user.username.lower() not in OWNER_USER:
                await self.bot.highrise.send_whisper(user.id, "Vous n'avez pas la permission pour utiliser cette commande.")
                return
                
            target_username = message[11:].strip()
            taskgroup = self.bot.highrise.tg
            task_list: list[Task] = list(taskgroup._tasks)
            for task in task_list:
                if task.get_name() == f"random_{target_username}":
                    task.cancel()
                    await self.bot.highrise.chat(f"Stopped random emotes for {target_username}")
                    return
            await self.bot.highrise.send_whisper(user.id, f"{target_username} is not doing random emotes")
            return

        # Check if message format is "{emote} @username"
        parts = message.split()
        if len(parts) == 2 and parts[1].startswith("@"):
            emote_query = parts[0]
            target_username = parts[1][1:]  # Remove @ symbol
            
            # Check permissions
            if user.username.lower() not in OWNER_USER:
                await self.bot.highrise.send_whisper(user.id, "Vous n'avez pas la permission pour utiliser cette commande.")
                return

            # Find the emote (by number or name)
            emote_id = None
            emote_name = None
            if emote_query.isdigit():
                emote_number = int(emote_query)
                for emote in self.emote_list:
                    if emote[0] == emote_number:
                        emote_id = emote[2]
                        emote_name = emote[1]
                        break
            else:
                # Try exact match first
                for emote in self.emote_list:
                    if emote[1].lower() == emote_query.lower():
                        emote_id = emote[2]
                        emote_name = emote[1]
                        break
                # If no exact match, try partial match
                if not emote_id:
                    for emote in self.emote_list:
                        if emote_query.lower() in emote[1].lower():
                            emote_id = emote[2]
                            emote_name = emote[1]
                            break

            if emote_id:
                # Get room users and find target user
                room_users = (await self.bot.highrise.get_room_users()).content
                target_user_id = None
                for room_user, _ in room_users:
                    if room_user.username.lower() == target_username.lower():
                        target_user_id = room_user.id
                        break
                
                if target_user_id:
                    await self.bot.highrise.send_emote(emote_id, target_user_id)
                    await self.bot.highrise.send_whisper(user.id, f"Made {target_username} perform emote [{emote_name}]")
                    return
                else:
                    await self.bot.highrise.send_whisper(user.id, f"User {target_username} not found in room")
                    return
            else:
                await self.bot.highrise.send_whisper(user.id, f"Invalid emote: {emote_query}")
                return

        # Original stop emote command
        if message.lower() in ["توقف", "stop"]:
            if user.id not in UserEmote_ids:
                await self.bot.highrise.send_whisper(user.id, "Sorry, you cannot use this command. Send a private message to the bot to activate its features!")
                return  
            await self.stopemote(user, message)
            return
        
        # Try to check if the message is a valid emote number or name
        emote_id = ""
        emote_name = ""

        # Check if the message is a number corresponding to a valid emote
        if message.isdigit():
            emote_number = int(message)
            for emote in self.emote_list:
                if emote[0] == emote_number:
                    emote_name = emote[1]
                    emote_id = emote[2]
                    break

        # Check if the message matches any emote name
        else:
            for emote in self.emote_list:
                if emote[1].lower() == message.lower():
                    emote_name = emote[1]
                    emote_id = emote[2]
                    break

        # If a valid emote is found, trigger the emote
        if emote_id != "":
            await self.emote(user, message)
        # Otherwise, ignore the message (allow normal chat without triggering "Invalid emote")


    async def emote(self, user: User, message: str) -> None:
        UserEmote_ids = self.load_UserEmote_ids()
        async def loop_emote(user: User, emote_name_or_number: str) -> None:
            emote_id = ""
            emote_name = ""

            # Check if the input is a number or a name
            if emote_name_or_number.isdigit():
                emote_number = int(emote_name_or_number)  # Input is a number
                for emote in self.emote_list:
                    if emote[0] == emote_number:
                        emote_name = emote[1]
                        emote_id = emote[2]
                        break
            else:
                # Input is a name
                for emote in self.emote_list:
                    if emote[1].lower() == emote_name_or_number.lower():
                        emote_name = emote[1]
                        emote_id = emote[2]
                        break

            if emote_id == "":
                await self.bot.highrise.send_whisper(user.id, "Invalid emote")
                return
            if user.id not in UserEmote_ids:
                await self.bot.highrise.send_whisper(user.id, "Sorry, you cannot use this command. Send a private message to the bot to activate its features!")
                return  

            await self.bot.highrise.send_whisper(user.id, f"You are looping [{emote_name}]! Type 'Stop' to stop emoting.")

            # Get the emote duration or use a default value
            sleep_duration = self.emote_durations.get(emote_name.lower(), 10)

            # Keep looping the emote regardless of the user's position
            while True:
                try:
                    await self.bot.highrise.send_emote(emote_id, user.id)
                except:
                    return
                await asyncio.sleep(sleep_duration)  # Wait for the duration of the emote before sending it again

        try:
            emote_name_or_number = message.strip()
        except:
            await self.bot.highrise.chat("Commande invalide format. Please use an emote name or number.")
            return
        else:
            taskgroup = self.bot.highrise.tg
            task_list: list[Task] = list(taskgroup._tasks)
            for task in task_list:
                if task.get_name() == user.username:
                    task.cancel()

            taskgroup.create_task(coro=loop_emote(user, emote_name_or_number))
            task_list: list[Task] = list(taskgroup._tasks)
            room_users = (await self.bot.highrise.get_room_users()).content
            user_list = [room_user.username for room_user, pos in room_users]
            for task in task_list:
                if task.get_coro().__name__ == "loop_emote" and task.get_name() not in user_list:
                    task.set_name(user.username)


    async def stopemote(self, user: User, message: str) -> None:
        taskgroup = self.bot.highrise.tg
        task_list: list[Task] = list(taskgroup._tasks)
        for task in task_list:
            if task.get_name() == user.username:
                task.cancel()
                await self.bot.highrise.send_whisper(user.id, "Stopping your emote loop!")
                return
        await self.bot.highrise.send_whisper(user.id, "You're not looping any emotes.")