from django import forms 


class FormFieldsController:
    fields = {}
    class_name = None
    disable_fields = False
    classes_excluded = []
    more_classes = {}
    placeholders = {}
    validators = []
    validators_excluded = []
    more_validators = {}
    help_text_to_remove = []
    widgets_attrs = {}
   
    def set_up_fields(self):
        if self.disable_fields:
            self.__disable_fields()

        if self.class_name is not None:
            self.__add_class_name_to_all_fields()

        self.__add_fields_classes()
        self.__add_placeholders()
        # self.__remove_labels()
        self.__add_validators()
        self.__add_widgets_attrs()
        self.__remove_help_text()
    
    def __add_class_name_to_all_fields(self):
        for field_name, field in self.fields.items():
            if field_name not in self.classes_excluded:
                if "class" not in field.widget.attrs:
                    field.widget.attrs["class"] = ""

                field.widget.attrs["class"] += f" {self.class_name} "
    
    def __add_fields_classes(self):
        for field, class_name in self.more_classes.items():
            if not self.fields.get(field):
                continue

            if "class" not in self.fields[field].widget.attrs:
                self.fields[field].widget.attrs["class"] = ""

            self.fields[field].widget.attrs["class"] += f" {class_name}"
    
    def __add_validators(self):
        for field_name, field in self.fields.items():
            if not field.validators:
                field.validators = []
            
            if field_name not in self.validators_excluded:
                field.validators.extend(self.validators)
        
        for field, validators in self.more_validators.items():
            if not self.fields.get(field):
                continue
            
            if not self.fields[field].validators:
                self.fields[field].validators = []
            self.fields[field].validators.extend(validators)     
    
    def __add_placeholders(self):
        for field, placeholder_name in self.placeholders.items():
            self.fields[field].widget.attrs["placeholder"] = placeholder_name


    def __add_widgets_attrs(self):
        for field, attrs in self.widgets_attrs.items():
            if not self.fields.get(field):
                continue

            if not getattr(self.fields[field].widget, "attrs"):
                self.fields[field].widget.attrs = {}

            self.fields[field].widget.attrs.update(attrs)
        
    def __remove_help_text(self):
        if self.help_text_to_remove == "__all__":
            self.help_text_to_remove = self.fields.keys()
             
        for fieldname in self.help_text_to_remove:
            self.fields[fieldname].help_text = None
        
    
    # def __remove_labels(self):
    #     if self.remove_labels == "__all__":
    #         self.remove_labels = self.fields.keys()

    #     for field in self.remove_labels:
    #         self.fields[field].label = ""