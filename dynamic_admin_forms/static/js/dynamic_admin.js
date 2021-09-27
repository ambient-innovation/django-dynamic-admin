var DynamicAdmin = {
    handleResponse: function(target, data) {
        data = JSON.parse(data);
        if (data.hidden) {
            target.parentNode.parentNode.classList.add("hidden");
        } else {
            target.parentNode.parentNode.classList.remove("hidden");
        }
        target.outerHTML = data.html;
    },

    dynamicSelect: function(app_label, model_name, field_name) {
        var $ = django.jQuery;
        var that = this;

        var form = $('#' + model_name + '_form');
        form.on(("change"), function() {
            $.post({
                url: "/dynamic-admin-form/" + app_label + "/" + model_name + "/" + field_name + "/",
                data: form.serialize(),
                success: function(data) {
                    var target = $(".field-" + field_name + " .related-widget-wrapper")[0];
                    that.handleResponse(target, data);
                }
            });
        });
    },

    dynamicInput: function(app_label, model_name, field_name) {
        var $ = django.jQuery;
        var that = this;

        var form = $('#' + model_name + '_form');
        form.on(("change"), function() {
            $.post({
                url: "/dynamic-admin-form/" + app_label + "/" + model_name + "/" + field_name + "/",
                data: form.serialize(),
                success: function(data) {
                    var target = $("#id_" + field_name)[0];
                    that.handleResponse(target, data);
                }
            });
        });
    },
}
