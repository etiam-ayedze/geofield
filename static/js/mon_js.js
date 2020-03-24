$(function () {
    $("#location_select").change(function () {
        var selectionne = $("#location_select option:selected ").text();
        $("select_value").val(selectionne);
    })
})

