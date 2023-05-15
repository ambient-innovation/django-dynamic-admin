var DynamicAdmin = {
  //# sourceURL="dynamic_admin.js"
  handleResponse: function (target, data) {
    var $ = django.jQuery;

    // set hidden class in parent form-row (or form-group if using jazzmin)
    if (data.hidden) {
      $(target.closest(".form-row,.form-group")).addClass("hidden");
    } else {
      $(target.closest(".form-row,.form-group")).removeClass("hidden");
    }

    // file fields will have this skipUpdate flag set
    // TODO It might be easier to just look at the type attribute of the input element...
    if (data.skipUpdate) {
      return;
    }

    // Update the options for the select widget (either select2 instance or normal select element)
    if ($(target).find("select").hasClass("select2-hidden-accessible")) {
      var select2Widget = $(target).find("select");
      var currentVal = select2Widget.val();
      var options = $($.parseHTML(data.html)).find("option");
      select2Widget.find("option").remove();
      select2Widget.append(options);
      select2Widget.val(currentVal);
    } else {
      target.outerHTML = data.html;
    }
  },

  dynamicWidgets: function (
    app_label,
    model_name,
    select_field_names,
    input_field_names
  ) {
    var $ = django.jQuery;
    var that = this;

    var $form = $("#" + model_name + "_form");

    $form.on("change", function () {
      var field_names = [...select_field_names, ...input_field_names];
      var params = new URLSearchParams([
        ["app_label", app_label],
        ["model_name", model_name],
        ...field_names.map((name) => ["field_names", name]),
      ]);
      var url = `/dynamic-admin-form/?${params}`;
      $.post({
        url,
        data: new FormData(this),
        contentType: false,
        processData: false,
        success: function (data) {
          snippets = JSON.parse(data);
          snippets.forEach(({ field_name, ...data }) => {
            if (select_field_names.indexOf(field_name) >= 0) {
              var target = $(
                ".field-" + field_name + " .related-widget-wrapper"
              )[0];
            } else {
              var target = $("#id_" + field_name)[0];
            }
            that.handleResponse(target, data);
          });
        },
      });
    });
  },
};
