$( document ).ready(function() {
    var listId = -1;
    var items = []
    $('#buildlist').hide();
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
        console.log(items);
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

    function listNameSet() {
        $('#buildlist').show();
        $('#savename').hide();
        $('#createlist').hide();
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