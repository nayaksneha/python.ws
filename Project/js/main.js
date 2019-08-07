$(document).ready((function() {

    $("#search").keyup(function(){
        searchStr = $("#search").val()
        if(searchStr.trim() != ""){
            showResult(searchStr);
        }
    })
}))

function showResult(searchStr){
    $.ajax({
        url: "https://fms-mite.herokuapp.com/fms/search/"+searchStr,
        method: "GET",
        success: function(data){
            showTable(data)
        }
    })

}

function showTable(data){
    str = "<table class = 'table'>";
    if(!data[0]){
        str += <center><h1>Not found</h1></center>
    }
    str += "<tr><th>Name</th><th>Qualification</th><th>Department</th><th>Status</th></tr>";

    for(i=0;i<data.length;i++){
        
        if(data[i]["qualification"] == ""){
            data[i]["qualification"] = "<small>Not found</small>"
        }
        str += "<tr>";
        str += "<td>"+data[i]["name"]+"</td>"
        str += "<td>"+data[i]["qualification"]+"</td>"
        str += "<td>"+data[i]["deptId"]+"</td>"
        str += "<td>"+data[i]["active"]+"</td>"
    }


    str += "</table>"
    $("#idTable").html(str);
}

$("#idViewAll").click(function(){
    $.ajax({
        url: "https://fms-mite.herokuapp.com/fms/",
        method : "GET",
        success : function(data){
            showTable(data);
        }
    })
})