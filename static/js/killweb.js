$(function() {
    var num=0
    var options1 = {    
	target:        '#result',   // target element(s) to be updated with server response    
	//beforeSubmit:  showRequest,  // pre-submit callback    
	success:       showResponse  // post-submit callback      
    }; 
    //$('#pagefm').ajaxForm(options);
    $('#pagefm').submit(function() {  
        $(this).ajaxSubmit(options1); 
        return false; 
    }); 

    function showResponse(responseText, statusText)  {
	$('#result').html("<a href="+responseText+">"+responseText+"</a>");
    }
    $( ".component" ).draggable(
	{appendTo: "body",
	 helper: "clone"});
    $( "#head-area").droppable({
	activeClass: "ui-state-default",
	hoverClass: "ui-state-hover",
	accept: ":not(.ui-sortable-helper)",
	drop: function( event, ui ) {
	    addelement("head",ui.draggable,$(this));
	}}).sortable({
	    items: "div:not(.placeholder)",
	    sort: function() {
		// gets added unintentionally by droppable interacting with sortable
		// using connectWithSortable fixes this, but doesn't allow you to customize active/hoverClass options
		$( this ).removeClass( "ui-state-default" );
	    }
	});
    $( "#body-area").droppable({
	activeClass: "ui-state-default",
	hoverClass: "ui-state-hover",
	accept: ":not(.ui-sortable-helper)",
	drop: function( event, ui ) {
	    addelement("body",ui.draggable,$(this));
	}}).sortable({
	    items: "li:not(.placeholder)",
	    sort: function() {
		// gets added unintentionally by droppable interacting with sortable
		// using connectWithSortable fixes this, but doesn't allow you to customize active/hoverClass options
		$( this ).removeClass( "ui-state-default" );
	    }
	});
    function options(type){
	switch (type){
	default:
	    code="code-"+num;
	    size="size-"+num;
	    time="time-"+num;
	    return $("<div class=config>response code:<input type=text length=15 value=200 name="+code+"><br>size:<input type=text length=15 value=100 name="+size+"><br>time:<input type=text length=15 value=0 name="+time+"></div>").hide();
	}
    }
    function addelement(section,$item,$parent){
	var delete_bt = $("<input type=button class=del-bt value=remove>");
	delete_bt.bind('click', function() {
	    $(this).parent().remove();
	});
	var param_bt =$("<input type=button class=param-bt value=params>");
	var type=$item.attr("name");
	var type_elem=$("<input type=hidden class=type-bt name=type-"+num+" value="+type+">");
	var section_elem=$("<input type=hidden class=section-bt name=section-"+num+" value="+section+">");
	param_bt.bind('click', function() {
	    $(this).parent().find(".config").toggle();
	});
	var elem=$( "<div></div>")
	    .append( $item.text())
	    .addClass($item.attr("class"))
	    .attr("id",$item.attr("name")+"div")
	    .append(section_elem)
	    .append(type_elem)
	    .append(options($item.attr("name")))
	    .append("<br>")
	    .append(delete_bt).append(param_bt).appendTo($parent);
	num++;
    }
});

