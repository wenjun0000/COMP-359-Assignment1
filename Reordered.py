#Implement a program that orders keys based on user query frequency during execution. 
#That is, upate the order over the use of the program so that sequential search operates faster.
'''
Pseudocode:
Initialize a list named keys containing the keys.
Initialize a dictionary frequenc to store query counts for each key.
Increment(key):
	If key exists in keys:
    	Increment frequency[key]
    	Call Resorting()
 
Resorting():
	Sort keys in descending order of their frequency from frequency dictionary.
 
Main Program:
	While user provides input:
    	Read the Increment(key)
    	Call Resorting(key)
    	Output the updated keys list
#Add timings for both optimal and non optimal searches
Things left to do in this code:
3. Test Large Data
4. Find Time Complexity, look for optimization
'''
import time

def Reorder(List, Dictionary):
    # Sort List based on Dictionary values in descending order
    List.sort(key=lambda x: Dictionary[x], reverse=True)

def sequential_search(List, key):
    # Perform a simple sequential search and return the number of comparisons made
    comparisons = 0
    for item in List:
        comparisons += 1
        if item == key:
            return comparisons
    return comparisons

Keys = ["Test1", "Test2", "Test3", "Test4", "Test5", "Test6", "Test7", "Test8", "Test9", "Test10",
"Test11", "Test12", "Test13", "Test14", "Test15", "Test16", "Test17", "Test18", "Test19", "Test20",
"Test21", "Test22", "Test23", "Test24", "Test25", "Test26", "Test27", "Test28", "Test29", "Test30",
"Test31", "Test32", "Test33", "Test34", "Test35", "Test36", "Test37", "Test38", "Test39", "Test40",
"Test41", "Test42", "Test43", "Test44", "Test45", "Test46", "Test47", "Test48", "Test49", "Test50",
"Test51", "Test52", "Test53", "Test54", "Test55", "Test56", "Test57", "Test58", "Test59", "Test60",
"Test61", "Test62", "Test63", "Test64", "Test65", "Test66", "Test67", "Test68", "Test69", "Test70",
"Test71", "Test72", "Test73", "Test74", "Test75", "Test76", "Test77", "Test78", "Test79", "Test80",
"Test81", "Test82", "Test83", "Test84", "Test85", "Test86", "Test87", "Test88", "Test89", "Test90",
"Test91", "Test92", "Test93", "Test94", "Test95", "Test96", "Test97", "Test98", "Test99", "Test100",
"Test101", "Test102", "Test103", "Test104", "Test105", "Test106", "Test107", "Test108", "Test109", "Test110",
"Test111", "Test112", "Test113", "Test114", "Test115", "Test116", "Test117", "Test118", "Test119", "Test120",
"Test121", "Test122", "Test123", "Test124", "Test125", "Test126", "Test127", "Test128", "Test129", "Test130",
"Test131", "Test132", "Test133", "Test134", "Test135", "Test136", "Test137", "Test138", "Test139", "Test140",
"Test141", "Test142", "Test143", "Test144", "Test145", "Test146", "Test147", "Test148", "Test149", "Test150",
"Test151", "Test152", "Test153", "Test154", "Test155", "Test156", "Test157", "Test158", "Test159", "Test160",
"Test161", "Test162", "Test163", "Test164", "Test165", "Test166", "Test167", "Test168", "Test169", "Test170",
"Test171", "Test172", "Test173", "Test174", "Test175", "Test176", "Test177", "Test178", "Test179", "Test180",
"Test181", "Test182", "Test183", "Test184", "Test185", "Test186", "Test187", "Test188", "Test189", "Test190",
"Test191", "Test192", "Test193", "Test194", "Test195", "Test196", "Test197", "Test198", "Test199", "Test200",
"Test201", "Test202", "Test203", "Test204", "Test205", "Test206", "Test207", "Test208", "Test209", "Test210",
"Test211", "Test212", "Test213", "Test214", "Test215", "Test216", "Test217", "Test218", "Test219", "Test220",
"Test221", "Test222", "Test223", "Test224", "Test225", "Test226", "Test227", "Test228", "Test229", "Test230",
"Test231", "Test232", "Test233", "Test234", "Test235", "Test236", "Test237", "Test238", "Test239", "Test240",
"Test241", "Test242", "Test243", "Test244", "Test245", "Test246", "Test247", "Test248", "Test249", "Test250",
"Test251", "Test252", "Test253", "Test254", "Test255", "Test256", "Test257", "Test258", "Test259", "Test260",
"Test261", "Test262", "Test263", "Test264", "Test265", "Test266", "Test267", "Test268", "Test269", "Test270",
"Test271", "Test272", "Test273", "Test274", "Test275", "Test276", "Test277", "Test278", "Test279", "Test280",
"Test281", "Test282", "Test283", "Test284", "Test285", "Test286", "Test287", "Test288", "Test289", "Test290",
"Test291", "Test292", "Test293", "Test294", "Test295", "Test296", "Test297", "Test298", "Test299", "Test300",
"Test301", "Test302", "Test303", "Test304", "Test305", "Test306", "Test307", "Test308", "Test309", "Test310",
"Test311", "Test312", "Test313", "Test314", "Test315", "Test316", "Test317", "Test318", "Test319", "Test320",
"Test321", "Test322", "Test323", "Test324", "Test325", "Test326", "Test327", "Test328", "Test329", "Test330",
"Test331", "Test332", "Test333", "Test334", "Test335", "Test336", "Test337", "Test338", "Test339", "Test340",
"Test341", "Test342", "Test343", "Test344", "Test345", "Test346", "Test347", "Test348", "Test349", "Test350",
"Test351", "Test352", "Test353", "Test354", "Test355", "Test356", "Test357", "Test358", "Test359", "Test360",
"Test361", "Test362", "Test363", "Test364", "Test365", "Test366", "Test367", "Test368", "Test369", "Test370",
"Test371", "Test372", "Test373", "Test374", "Test375", "Test376", "Test377", "Test378", "Test379", "Test380",
"Test381", "Test382", "Test383", "Test384", "Test385", "Test386", "Test387", "Test388", "Test389", "Test390",
"Test391", "Test392", "Test393", "Test394", "Test395", "Test396", "Test397", "Test398", "Test399", "Test400",
"Test401", "Test402", "Test403", "Test404", "Test405", "Test406", "Test407", "Test408", "Test409", "Test410",
"Test411", "Test412", "Test413", "Test414", "Test415", "Test416", "Test417", "Test418", "Test419", "Test420",
"Test421", "Test422", "Test423", "Test424", "Test425", "Test426", "Test427", "Test428", "Test429", "Test430",
"Test431", "Test432", "Test433", "Test434", "Test435", "Test436", "Test437", "Test438", "Test439", "Test440",
"Test441", "Test442", "Test443", "Test444", "Test445", "Test446", "Test447", "Test448", "Test449", "Test450",
"Test451", "Test452", "Test453", "Test454", "Test455", "Test456", "Test457", "Test458", "Test459", "Test460",
"Test461", "Test462", "Test463", "Test464", "Test465", "Test466", "Test467", "Test468", "Test469", "Test470",
"Test471", "Test472", "Test473", "Test474", "Test475", "Test476", "Test477", "Test478", "Test479", "Test480",
"Test481", "Test482", "Test483", "Test484", "Test485", "Test486", "Test487", "Test488", "Test489", "Test490",
"Test491", "Test492", "Test493", "Test494", "Test495", "Test496", "Test497", "Test498", "Test499", "Test500",
"Test501", "Test502", "Test503", "Test504", "Test505", "Test506", "Test507", "Test508", "Test509", "Test510",
"Test511", "Test512", "Test513", "Test514", "Test515", "Test516", "Test517", "Test518", "Test519", "Test520",
"Test521", "Test522", "Test523", "Test524", "Test525", "Test526", "Test527", "Test528", "Test529", "Test530",
"Test531", "Test532", "Test533", "Test534", "Test535", "Test536", "Test537", "Test538", "Test539", "Test540",
"Test541", "Test542", "Test543", "Test544", "Test545", "Test546", "Test547", "Test548", "Test549", "Test550",
"Test551", "Test552", "Test553", "Test554", "Test555", "Test556", "Test557", "Test558", "Test559", "Test560",
"Test561", "Test562", "Test563", "Test564", "Test565", "Test566", "Test567", "Test568", "Test569", "Test570",
"Test571", "Test572", "Test573", "Test574", "Test575", "Test576", "Test577", "Test578", "Test579", "Test580",
"Test581", "Test582", "Test583", "Test584", "Test585", "Test586", "Test587", "Test588", "Test589", "Test590",
"Test591", "Test592", "Test593", "Test594", "Test595", "Test596", "Test597", "Test598", "Test599", "Test600",
"Test601", "Test602", "Test603", "Test604", "Test605", "Test606", "Test607", "Test608", "Test609", "Test610",
"Test611", "Test612", "Test613", "Test614", "Test615", "Test616", "Test617", "Test618", "Test619", "Test620",
"Test621", "Test622", "Test623", "Test624", "Test625", "Test626", "Test627", "Test628", "Test629", "Test630",
"Test631", "Test632", "Test633", "Test634", "Test635", "Test636", "Test637", "Test638", "Test639", "Test640",
"Test641", "Test642", "Test643", "Test644", "Test645", "Test646", "Test647", "Test648", "Test649", "Test650",
"Test651", "Test652", "Test653", "Test654", "Test655", "Test656", "Test657", "Test658", "Test659", "Test660",
"Test661", "Test662", "Test663", "Test664", "Test665", "Test666", "Test667", "Test668", "Test669", "Test670",
"Test671", "Test672", "Test673", "Test674", "Test675", "Test676", "Test677", "Test678", "Test679", "Test680",
"Test681", "Test682", "Test683", "Test684", "Test685", "Test686", "Test687", "Test688", "Test689", "Test690",
"Test691", "Test692", "Test693", "Test694", "Test695", "Test696", "Test697", "Test698", "Test699", "Test700",
"Test701", "Test702", "Test703", "Test704", "Test705", "Test706", "Test707", "Test708", "Test709", "Test710",
"Test711", "Test712", "Test713", "Test714", "Test715", "Test716", "Test717", "Test718", "Test719", "Test720",
"Test721", "Test722", "Test723", "Test724", "Test725", "Test726", "Test727", "Test728", "Test729", "Test730",
"Test731", "Test732", "Test733", "Test734", "Test735", "Test736", "Test737", "Test738", "Test739", "Test740",
"Test741", "Test742", "Test743", "Test744", "Test745", "Test746", "Test747", "Test748", "Test749", "Test750",
"Test751", "Test752", "Test753", "Test754", "Test755", "Test756", "Test757", "Test758", "Test759", "Test760",
"Test761", "Test762", "Test763", "Test764", "Test765", "Test766", "Test767", "Test768", "Test769", "Test770",
"Test771", "Test772", "Test773", "Test774", "Test775", "Test776", "Test777", "Test778", "Test779", "Test780",
"Test781", "Test782", "Test783", "Test784", "Test785", "Test786", "Test787", "Test788", "Test789", "Test790",
"Test791", "Test792", "Test793", "Test794", "Test795", "Test796", "Test797", "Test798", "Test799", "Test800",
"Test801", "Test802", "Test803", "Test804", "Test805", "Test806", "Test807", "Test808", "Test809", "Test810",
"Test811", "Test812", "Test813", "Test814", "Test815", "Test816", "Test817", "Test818", "Test819", "Test820",
"Test821", "Test822", "Test823", "Test824", "Test825", "Test826", "Test827", "Test828", "Test829", "Test830",
"Test831", "Test832", "Test833", "Test834", "Test835", "Test836", "Test837", "Test838", "Test839", "Test840",
"Test841", "Test842", "Test843", "Test844", "Test845", "Test846", "Test847", "Test848", "Test849", "Test850",
"Test851", "Test852", "Test853", "Test854", "Test855", "Test856", "Test857", "Test858", "Test859", "Test860",
"Test861", "Test862", "Test863", "Test864", "Test865", "Test866", "Test867", "Test868", "Test869", "Test870",
"Test871", "Test872", "Test873", "Test874", "Test875", "Test876", "Test877", "Test878", "Test879", "Test880",
"Test881", "Test882", "Test883", "Test884", "Test885", "Test886", "Test887", "Test888", "Test889", "Test890",
"Test891", "Test892", "Test893", "Test894", "Test895", "Test896", "Test897", "Test898", "Test899", "Test900",
"Test901", "Test902", "Test903", "Test904", "Test905", "Test906", "Test907", "Test908", "Test909", "Test910",
"Test911", "Test912", "Test913", "Test914", "Test915", "Test916", "Test917", "Test918", "Test919", "Test920",
"Test921", "Test922", "Test923", "Test924", "Test925", "Test926", "Test927", "Test928", "Test929", "Test930",
"Test931", "Test932", "Test933", "Test934", "Test935", "Test936", "Test937", "Test938", "Test939", "Test940",
"Test941", "Test942", "Test943", "Test944", "Test945", "Test946", "Test947", "Test948", "Test949", "Test950",
"Test951", "Test952", "Test953", "Test954", "Test955", "Test956", "Test957", "Test958", "Test959", "Test960",
"Test961", "Test962", "Test963", "Test964", "Test965", "Test966", "Test967", "Test968", "Test969", "Test970",
"Test971", "Test972", "Test973", "Test974", "Test975", "Test976", "Test977", "Test978", "Test979", "Test980",
"Test981", "Test982", "Test983", "Test984", "Test985", "Test986", "Test987", "Test988", "Test989", "Test990",
"Test991", "Test992", "Test993", "Test994", "Test995", "Test996", "Test997", "Test998", "Test999", "Test1000"]

Frequency = {key: 0 for key in Keys}

while True:

    
    Inp = input("Enter your input: ")

    start_time = time.time()

    if Inp in Keys:
        # Increment frequency for existing key
        Frequency[Inp] += 1
    else:
        # Add new key and set its frequency to 1
        Keys.append(Inp)
        Frequency[Inp] = 1

    # Reorder keys based on frequency
    Reorder(Keys, Frequency)

    # Measure time and number of comparisons for search
    comparisons = sequential_search(Keys, Inp)
    end_time = time.time()

    # Calculate time taken
    time_taken = end_time - start_time

    # Display search results
    print(f"Time taken to search: {time_taken:.8f} seconds")
    print(f"Number of comparisons: {comparisons}")
