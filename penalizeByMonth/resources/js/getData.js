var TABLE_DATA;
var ASEC = false;
var NOW_PAGE = 1;

//切换每页数据条数
$('select').change(function(event){
    addDataToTable(TABLE_DATA);
});

//翻页
$('a').click(function(){
    var id = $(this).attr('id');
    var onePageNumber = $('select').children('option:selected').val();
    var data_length = TABLE_DATA.length;
    var total_page = parseInt(data_length / onePageNumber) + 1;
    NOW_PAGE = id == 'first' && 1 || id == 'previous' && (NOW_PAGE - 1 || 1) || id == 'next' && NOW_PAGE + 1 || total_page;
    NOW_PAGE > total_page && (NOW_PAGE = total_page)
    addDataToTable(TABLE_DATA, '', NOW_PAGE);
});


//点击表头排序
$('thead th').click(function(){
    var id=$(this).attr('id');
    id = id && id.split('-')[1];
    TABLE_DATA.sort(function(x, y){
        if(id == 0)
            if(ASEC == false)
                return y[0].replace('-','') - x[0].replace('-', '');
            else
                return x[0].replace('-','') - y[0].replace('-', '');
        else
            if(ASEC == false)
                return y[id] - x[id];
            else
                return x[id] - y[id];
    });
    ASEC = !ASEC;
    addDataToTable(TABLE_DATA);
});

//查询
$('#query').click(function(){
    var start = $('#start').val();
    var end = $('#end').val();
    getData(start, end);
});


//向后台请求获取数据
function getData(start, end){
    var now_date = new Date();
    var year = now_date.getFullYear();
    var month = now_date.getMonth();
    month = month < 10 ? '0' + month : month;
    var date = year + '-' + month;
    end  = end || date;
    start = start || '';
    $.ajax({
        type: 'post',
        url: '../homePage/getPunishDataAction.do',
        data: {'start': start, 'end': end},
        dataType: 'json',
        async: true,
        success: function(data){
            var table_data = constructTableData(data);
            table_data.sort(function(x, y){
                return y[0].replace('-','') - x[0].replace('-', '');
            });
            addDataToTable(table_data);
            var map_data = constructMapData(data);
            initEcharts(map_data);
        },
        error: function(data){
            console.log('Error');
            addDataToTable();
            initEcharts();
        }
    });
}

//初始化echarts图
function initEcharts(data){
    var map_punish = echarts.init(document.getElementById('div-map'));
    var option = new option_echarts();
    if (!data) {
        map_punish.setOption(option);
        return;
    }
    option.xAxis.data = data.time;
    option.series[0].data = data.penalty;
    option.series[1].data = data.number;
    map_punish.setOption(option);
}

//构造echart需要的数据
function constructMapData(data){
    var number = data.number;
    var penalty = data.penalty;
    var time = [];
    var map_number = [];
    var map_penalty = [];
    for(var key in number){
        time.push(key);
        var total_number = 0;
        var total_penalty = 0;
        for(var i = 0; i < 4; i++){
            total_number += parseInt(number[key][i]);
            total_penalty += parseInt(penalty[key][i]);
        }
        map_number.push(total_number);
        map_penalty.push(total_penalty);
    }
    var map_data = {};
    map_data['time'] = time;
    map_data['number'] = map_number;
    map_data['penalty'] = map_penalty;
    return map_data;
}

//构造表格需要的数据
function constructTableData(data){
    var number = data.number;
    var penalty = data.penalty;
    var table_data = [];
    for(var key in number){
        var th_info_number = number[key];
        var th_info_penalty = penalty[key];
        var th_data = [];
        th_data.push(key);
        for(var i = 0; i < 4; i++){
            th_data.push(th_info_number[i]);
            th_data.push(th_info_penalty[i]);
        }
        table_data.push(th_data);
    }
    TABLE_DATA = table_data;
    return table_data;
}

//将数据添加到页面表格中
function addDataToTable(data, onePageNumber, pageNumber){
    onePageNumber = $('select').children('option:selected').val();
    onePageNumber = onePageNumber == 'all' && data.length || onePageNumber;
    pageNumber = pageNumber || 1;
    $('tbody').empty();
    var th_data = '';
    data || (data = []);
    for(var j = (pageNumber - 1) * onePageNumber; j < data.length; j++){
        th_data = '';
        th_data += j % 2 == 0 ? '<tr class="single">' : '<tr class="double">';
        for(var k = 0; k < data[j].length; k ++){
            th_data += '<th>' + data[j][k] + '</th>';
        }
        th_data += '</tr>';
        $('tbody').append(th_data);
        if(j == onePageNumber * pageNumber - 1)
            break;
    }
    var start = (pageNumber - 1) * onePageNumber + 1;
    var end = onePageNumber * pageNumber > data.length ? data.length : onePageNumber * pageNumber;
    var str = '从 ' + start + ' 到' + end + ' /共 ' + data.length + ' 条数据'
    $('.table-footer-left').text(str);
    
    data.length == 0 && (th_data = '<tr class="single"><th>没有记录</th></tr>', 
            $('tbody').append(th_data), 
            str = '从  0  到 0 /共 ' + data.length + ' 条数据', 
            $('.table-footer-left').text(str));
    
//  动态设置表格高度
    var tr_height = $('tbody tr').height();
    var tbody_height = tr_height * (end - start + 1);
    $('tbody').css('height', tbody_height);
    var top_main_left = $('#main-left').offset().top;
    var height_main_left = $('#main-left').height();
    var top_tbody = $('tbody').offset().top;
    var free_height = height_main_left - (top_tbody - top_main_left) - 20;
    tbody_height < free_height ? ($('tbody').removeClass('scroll-tbody').css('height', tbody_height), $('thead').removeClass('thead-cal')) : 
        ($('tbody').addClass('scroll-tbody').css('height', free_height), $('thead').addClass('thead-cal'));
}



var option_echarts = function() {
return {
    title : {
        text : '进出港船舶变化趋势',
        textStyle : {
            fontWeight : 'bold',
            fontSize : 16,
            fontFamily : 'Microsoft YaHei',
            color : '#F1F1F3'
        },
        left : '34%',
        top : '2%',
    },
    tooltip : {
        trigger : 'axis',
        textStyle : {
            align : 'left'
        }
    },
    legend : {
        top : '9%',
        left: '20%',
        data : ['处罚数', '罚款'],
        icon : 'circle',
        textStyle : {
            color : "#ffffff"
        }
    },
    grid : {
        top : '25%',
        left : '3%',
        right : '6%',
        bottom : '10%',
        containLabel : true
    },
    xAxis : {
        type : 'category',
        boundaryGap : true,
        data : [],
        "axisLabel" : {
            "show" : true,
            interval : 0,
            "textStyle" : {
                "color" : "#3dd3f8"
            }
        }
    },
    yAxis : [ {
        type : 'value',
        name : '处罚数(件)',
        nameTextStyle : {
            color : '#fff',
        },
        axisLabel : {
            formatter : '{value} ',
            interval : 0,
            "textStyle" : {
                "color" : "#3dd3f8"
            }
        },
        //min : 100,

        "splitLine" : {
            "lineStyle" : {
                "color" : "#7d838b"
            }
        }
    },
    {
        type : 'value',
        name : '罚款(元)',
        nameTextStyle : {
            color : '#fff',
        },
        axisLabel : {
            formatter : '{value} ',
            interval : 0,
            "textStyle" : {
                "color" : "#3dd3f8"
            }
        },
        //min : 100,
    } ],
    dataZoom : [ {
        type : 'inside',
        start : 60,
        end : 100
    }, {
        show : true,
        type : 'slider',
        y : '90%',
        start : 50,
        end : 100,
        "textStyle" : {
            "color" : "#3dd3f8"
        }
    } ],
    series : [
    {
        type: 'line',
        name: '罚款',
        yAxisIndex : 1,
        lineStyle: {
            normal: {
                width: 2,
            }
        },
        smooth: true,
        data: [],
    },
    {
        type: 'bar',
        name: '处罚数',
        barWidth: 20,
        itemStyle:{
          normal:{
              color:'#0288D1',
          },
        },
        data: [],
    },
    ]
}
};