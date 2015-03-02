#!/usr/bin/python
from gi.repository import Gtk, Gio

class HeaderBarWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Stack Demo")
        self.set_border_width(10)
        # self.set_default_size(400, 200)
        self.set_resizable(False)

        hb = Gtk.HeaderBar()
        hb.set_show_close_button(True)
        hb.props.title = "Metabolismo"
        hb.props.subtitle = "Appdietetica"
        self.set_titlebar(hb)

        button = Gtk.Button()
        icon = Gio.ThemedIcon(name="open-menu-symbolic")
        image = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)
        button.add(image)
        hb.pack_end(button)
        
        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        Gtk.StyleContext.add_class(box.get_style_context(), "linked") # hace que los botones esten agrupados

        # button = Gtk.Button()
        # button.add(Gtk.Arrow(Gtk.ArrowType.LEFT, Gtk.ShadowType.NONE))
        # box.add(button)

        # button = Gtk.Button()
        # button.add(Gtk.Arrow(Gtk.ArrowType.RIGHT, Gtk.ShadowType.NONE))
        # box.add(button)

        hb.pack_start(box)
        

        grid = Gtk.Grid(column_spacing=10, row_spacing=5)
        self.add(grid)


        # LABELS
        sexo_label = Gtk.Label(label="Sexo")
        sexo_label.set_alignment(0, 0.5)
        edad_label = Gtk.Label(label="Edad")
        edad_label.set_alignment(0, 0.5)
        peso_label = Gtk.Label(label="Peso (Kg)")
        peso_label.set_alignment(0, 0.5)
        altura_label = Gtk.Label(label="Altura (cm)")
        altura_label.set_alignment(0, 0.5)
        actividad_label = Gtk.Label(label="Actividad")
        actividad_label.set_alignment(0, 0.5)
        enfermedad_label = Gtk.Label(label="Enfermedad")
        enfermedad_label.set_alignment(0, 0.5)
        basal_label = Gtk.Label(use_markup=True, label="<b>Basal</b>")
        basal_label.set_alignment(0, 0.5)
        total_label = Gtk.Label(use_markup=True, label="<b>Total</b>")
        total_label.set_alignment(0, 0.5)
        self.res_basal_label = Gtk.Label(use_markup=True, label="<b>1200 kcal x ej</b>")
        self.res_total_label = Gtk.Label(use_markup=True, label="<b>1200 kcal x ej</b>")

        sexo_list = Gtk.ListStore(str)
        sex_opt = ["Hombre", "Mujer", "Mujer (embarazo 1º trimestre)", "Mujer (embarazo 2-3º trimestre)", "Mujer (estado de lactancia)"]
        for opt in sex_opt:
            sexo_list.append([opt])

        self.sexo_combo = Gtk.ComboBox.new_with_model(sexo_list)
        self.sexo_combo.connect("changed", self.on_calcularmb_button_clicked) 
        renderer_text = Gtk.CellRendererText()
        self.sexo_combo.pack_start(renderer_text, True)
        self.sexo_combo.add_attribute(renderer_text, "text", 0)

        actividad_list = Gtk.ListStore(str)
        actividad_opt = ["Sedentaria", "Ligera (1-3 días por semana)", "Moderada (3-5 días por semana)", "Intensa (6-7 días por semana)", "Muy intensa (2h/día)"]
        for opt in actividad_opt:
            actividad_list.append([opt])

        self.actividad_combo = Gtk.ComboBox.new_with_model(actividad_list)
        self.actividad_combo.connect("changed", self.on_calcularmb_button_clicked )
        renderer_text = Gtk.CellRendererText()
        self.actividad_combo.pack_start(renderer_text, True)
        self.actividad_combo.add_attribute(renderer_text, "text", 0)

        enfermedad_list = Gtk.ListStore(str)
        enfermedad_opt = ["Sano", "Leve", "Moderada", "Grave", "Neumonía", "Politraumatizado", "Sepsis", "Quemaduras"]
        for opt in enfermedad_opt:
            enfermedad_list.append([opt])

        self.enfermedad_combo = Gtk.ComboBox.new_with_model(enfermedad_list)
        self.enfermedad_combo.connect("changed", self.on_calcularmb_button_clicked)
        renderer_text = Gtk.CellRendererText()
        self.enfermedad_combo.pack_start(renderer_text, True)
        self.enfermedad_combo.add_attribute(renderer_text, "text", 0)

        self.edad_spin = Gtk.SpinButton(adjustment=Gtk.Adjustment(0, 0, 120, 1, 0, 0))
        self.edad_spin.connect("changed", self.on_calcularmb_button_clicked)
        self.peso_spin = Gtk.SpinButton(adjustment=Gtk.Adjustment(0, 0, 300, 1, 0, 0))
        self.peso_spin.connect("changed", self.on_calcularmb_button_clicked)
        self.altura_spin = Gtk.SpinButton(adjustment=Gtk.Adjustment(0, 0, 220, 1, 0, 0))
        self.altura_spin.connect("changed", self.on_calcularmb_button_clicked)

        calcularmb_button = Gtk.Button(label="Calcular metabolismo")
        Gtk.StyleContext.add_class(calcularmb_button.get_style_context(), "suggested-action") # color azul
        # Gtk.StyleContext.add_class(calcularmb_button.get_style_context(), "destructive-action") # color rojo

        grid.attach(sexo_label, 0, 0, 1, 1)
        grid.attach(self.sexo_combo, 1, 0, 1, 1)
        grid.attach(edad_label, 0, 1, 1, 1)
        grid.attach(self.edad_spin, 1, 1, 1, 1)
        grid.attach(peso_label, 0, 2, 1, 1)
        grid.attach(self.peso_spin, 1, 2, 1, 1)
        grid.attach(altura_label, 0, 3, 1, 1)
        grid.attach(self.altura_spin, 1, 3, 1, 1)
        grid.attach(actividad_label, 0, 4, 1, 1)
        grid.attach(self.actividad_combo, 1, 4, 1, 1)
        grid.attach(enfermedad_label, 0, 5, 1, 1)
        grid.attach(self.enfermedad_combo, 1, 5, 1, 1)
        grid.attach(basal_label, 0, 6, 1, 1)
        grid.attach(self.res_basal_label, 1, 6, 1, 1)
        grid.attach(total_label, 0, 7, 1, 1)
        grid.attach(self.res_total_label, 1, 7, 1, 1)

    def on_calcularmb_button_clicked(self, button):
        # widget.set_label("MB")
        actividad = self.actividad_combo.get_active()
        # print(actividad)
        sexo = self.sexo_combo.get_active()
        # print(sexo)
        enfermedad = self.enfermedad_combo.get_active()
        # print(enfermedad)
        edad = self.edad_spin.get_value()
        print(edad)
        peso = self.peso_spin.get_value()
        print(peso)
        altura = self.altura_spin.get_value()
        print(altura)
        if altura > 0:
            print("altura es mayor que 0")
        if sexo != -1 and enfermedad != -1 and actividad != -1 and altura != 0 and peso != 0 and edad != 0:
            print("rellenado")
            self.res_total_label.set_label("MT")
            self.res_basal_label.set_label("MB")
            # TODO peso poner como float y altura también como metro mejor
            # TODO implementar la lógica para el cálculo

win = HeaderBarWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
