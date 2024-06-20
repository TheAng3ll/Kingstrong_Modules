odoo.define('Kingstrong_extended', function (require) {
    "use strict";

    var FormView = require('web.FormView');

    FormView.include({
        render_field: function (field_name) {
            this._super.apply(this, arguments);
            if (field_name === 'document_origin') {
                this.$el.find('input[name="origin"]').attr('disabled', 'disabled').css('opacity', '0.5');
            }
        },
    });
});