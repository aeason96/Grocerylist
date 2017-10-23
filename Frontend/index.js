$( document ).ready(function() {
    var listId = -1;
    var items = []
    $('#buildlist').hide();
    $('#buildlist2').hide();
    setSelectDropdown();

    function setSelectDropdown() {
        $.ajax({
            type: "GET",
            url: "http://localhost:8000/api/grocerylists/",
            success: function(ret) {
                var dropdown = $('#loadlist');
                dropdown.empty();
                dropdown.append('<option>Select a List</option>');
                for (var i in ret) {
                    dropdown.append('<option value=\"' + ret[i]['id'] + '\">' + ret[i]['name'] + '</option>')
                }
            }
        });
    }

    $('#loadlist').change(function() {
        setItemsByListId($('#loadlist').val());
        listId = $('#loadlist').val();
        $('#buildlist2').show();
    });

    function setItemsByListId(id) {
        $.ajax({
            type: "GET",
            url: "http://localhost:8000/api/groceryitems/grocerylist/" + id + "/",
            success: function(ret) {
                items = []
                $('#loadedlist').empty();
                for (var i in ret) {
                    items.push(ret[i]['name'])
                    $('#loadedlist').append('<li>' + items[i] + '</li>');
                }
            }
        });
    }

    $('#saveitem2').click(function() {
        var name = $('#newitem2').val().toString();
        console.log(name + ' ' + listId);
        $.ajax({
            type: "POST",
            url: "http://localhost:8000/api/groceryitems/",
            data: {'name':name, 'grocerylist':listId},
            success: function(ret) {
                $('#loadedlist').append('<li>' + name+ '</li>');
            }
        });
    });

    function listNameSet() {
        $('#buildlist').show();
        //$('#savename').hide();
        //$('#createlist').hide();
        $('#listtitle').show();
    }

    $('#savename').click(function() {
        var name = $('#listname').val();
        $.ajax({
            type: "POST",
            url: "http://localhost:8000/api/grocerylists/",
            data: {'name':name},
            success: function(ret) {
                listId = ret['id'];
                $('#listtitle').empty();
                $('#grocerylist').empty();
                $('#listtitle').append(name);
                listNameSet();
                setSelectDropdown();
            }
        });
    })

    $('#saveitem').click(function() {
        var name = $('#newitem').val().toString();
        $.ajax({
            type: "POST",
            url: "http://localhost:8000/api/groceryitems/",
            data: {'name':name, 'grocerylist':listId},
            success: function(ret) {
                $('#grocerylist').append('<li>' + name+ '</li>');
            }
        });
    });


});