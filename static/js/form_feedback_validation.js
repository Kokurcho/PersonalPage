// Wait for the DOM to be ready
$(function() {
    // Initialize form validation on the registration form.
    // It has the name attribute "registration"
    $("form[name='feedback']").validate({
   // Specify validation rules
   rules: {
   // The key name on the left side is the name attribute
   // of an input field. Validation rules are defined
   // on the right side
   firstname: "required",
   message: "required",
   },
   // Specify validation error messages
   messages: {
   firstname: "Введите имя",
   message: "Введите ваши пожелания",
   },
   // Make sure the form is submitted to the destination defined
   // in the "action" attribute of the form when valid
   submitHandler: function(form) {
   form.submit();
   }
    });
  });