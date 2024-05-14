import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import IntVar, StringVar, filedialog, messagebox
import sqlite3

win = tk.Tk()

WIDTH = win.winfo_screenwidth()
HEIGHT = win.winfo_screenheight()

win.title("Second ChildHood")
win.geometry(f"{WIDTH}x{HEIGHT}")


def first_page():
    first_frame = tk.Frame(win, width=WIDTH, height=HEIGHT)
    
    def inner_first_page():
        image1 = Image.open("shantai_original.jpg")
        resized_image2 = image1.resize((WIDTH, HEIGHT))
        img = ImageTk.PhotoImage(resized_image2)

        # Create a Label Widget to display the text or Image
        label1 = tk.Label(win, image = img)
        label1.image = img
        label1.place(x=0, y=0)

        frame1 = tk.Frame(label1, width=500, height=500, bg='#D6D7E8')
        frame1.place(relx=0.5, rely=0.5, anchor='center')
        

        # Username section
        username_label = tk.Label(frame1, text="Username", font=("Ariel", 18), bg='#D6D7E8')
        username_label.place(x=25, y=40)

        username_entry = tk.Entry(frame1, width=34, font=("Ariel", 18))
        username_entry.place(x=25,y=80)


        # Password section
        password_label = tk.Label(frame1, text="Password", font=("Ariel", 18), bg='#D6D7E8')
        password_label.place(x=25, y=180)


        password_entry = tk.Entry(frame1, width=34, font=("Ariel", 18))
        password_entry.place(x=25, y=220)

        def after_login():
            def add_information():
                add_information_frame = tk.Frame(win, width=WIDTH, height=HEIGHT)
                add_information_frame.place(x=0, y=0)

                # residence information label
                residence_label = tk.Label(add_information_frame, text="New Residence Information", font=("Times New Roman", 50), fg="purple")
                residence_label.place(x=400, y=30)

                # Name lable
                name_label = tk.Label(add_information_frame, text="Name", font=("Times New Roman", 20))
                name_label.place(x=50, y=130)

                # Name entry
                name_entry = tk.Entry(add_information_frame, font=("Times New Roman", 20), width=36)
                name_entry.place(x=150, y=130)

                # Age label
                age_label = tk.Label(add_information_frame, text="Age", font=("Times New Roman", 20))
                age_label.place(x=50, y=230)

                # Age entry
                age_entry = tk.Entry(add_information_frame, font=("Times New Roman", 20), width=36)
                age_entry.place(x=150, y=230)

                # Gender label
                gender_label = tk.Label(add_information_frame, text="Gender", font=("Times New Roman", 20))
                gender_label.place(x=50, y=330)


                gender = StringVar()
                gender.set("Male")

                # Gender Male
                gender_male = tk.Radiobutton(add_information_frame, text="Male", value="Male", variable=gender, font=("Times New Roman", 18))
                gender_male.place(x=150, y=330)

                # Gender Female
                gender_female = tk.Radiobutton(add_information_frame, text="Female", value="Female", variable=gender, font=("Times New Roman", 18))
                gender_female.place(x=270, y=330)

                # Gender Other
                gender_other = tk.Radiobutton(add_information_frame, text="Other", value="Other", variable=gender, font=("Times New Roman", 18))
                gender_other.place(x=400, y=330)


                # Address line 1 label
                address_line_1_label = tk.Label(add_information_frame, text="Address Line 1", font=("Times New Roman", 20))
                address_line_1_label.place(x=750, y=130)


                line_1 = StringVar()



                # Address line 1 entry
                address_line_1_entry = tk.Entry(add_information_frame, font=("Times New Roman", 20), width=36, textvariable=line_1)
                address_line_1_entry.place(x=950, y=130)

                # Address line 2 label
                address_line_2_label = tk.Label(add_information_frame, text="Address Line 2", font=("Times New Roman", 20))
                address_line_2_label.place(x=750, y=230)


                line_2 = StringVar()


                # Address line 2 entry
                address_line_2_entry = tk.Entry(add_information_frame, font=("Times New Roman", 20), width=36, textvariable=line_2)
                address_line_2_entry.place(x=950, y=230)

                # Aadhar number label
                adhar_label = tk.Label(add_information_frame, text="Adhar", font=("Times New Roman", 20))
                adhar_label.place(x=750, y=330)


                # Aadhar number entry
                adhar_entry = tk.Entry(add_information_frame, font=("Times New Roman", 20), width=36)
                adhar_entry.place(x=950, y=330)

                # mobile number label
                mobile_label = tk.Label(add_information_frame, text="Mobile", font=("Times New Roman", 20))
                mobile_label.place(x=750, y=430)


                # mobile number entry
                mobile_entry = tk.Entry(add_information_frame, font=("Times New Roman", 20), width=36)
                mobile_entry.place(x=950, y=430)

                # Registration Date label
                date_label = tk.Label(add_information_frame, text="Registration Date", font=("Times New Roman", 20))
                date_label.place(x=50, y=430)


                # day label
                day_label = tk.Label(add_information_frame, text="Day", font=("Times New Roman", 20))
                day_label.place(x=50, y=480)

                
                
                # day entry
                day_entry = tk.Entry(add_information_frame, font=("Times New Roman", 20), width=8)
                day_entry.place(x=100, y=480)

                # month label
                month_label = tk.Label(add_information_frame, text="Month", font=("Times New Roman", 20))
                month_label.place(x=225, y=480)



                # month entry
                month_entry = tk.Entry(add_information_frame, font=("Times New Roman", 20), width=8)
                month_entry.place(x=325, y=480)


                # # year label
                year_label = tk.Label(add_information_frame, text="Year", font=("Times New Roman", 20))
                year_label.place(x=465, y=480)



                # year entry
                year_entry = tk.Entry(add_information_frame, font=("Times New Roman", 20), width=8)
                year_entry.place(x=540, y=480)

               


                def get_all_registration_info():
                    Name = name_entry.get()
                    Age = age_entry.get()

                    Gender = gender.get()
                    # Relation = relation.get()
                    # Pention = pention.get()
                    # Operation = operation.get()

                    Day = day_entry.get()
                    Month = month_entry.get()
                    Year = year_entry.get()

                    Line_1 = line_1.get()
                    Line_2 = line_2.get()
                    Adhar = adhar_entry.get()
                    Mobile = mobile_entry.get()

                    def check_info(val):
                        for i in range(len(val)):
                            if Name[i].isnumeric() == True:
                                return True


                    # validation
                    if Name.isnumeric() == True or Name == "" or check_info(Name) == True:
                        messagebox.showerror("Error", "Please Enter Valid Name")
                        name_entry.delete(0, 'end')
                    elif Age.isnumeric() == False or Age == "":
                        messagebox.showerror("Error", "Please Enter Valid Age")
                        age_entry.delete(0, 'end')
                    elif Day.isnumeric() == False or Day == "" or int(Day) >= 32:
                        messagebox.showerror("Error", "Please Enter Valid Day")
                        day_entry.delete(0, 'end')
                    elif Month.isnumeric() == False or Month == "" or int(Month) >= 13:
                        messagebox.showerror("Error", "Please Enter Valid Month")
                        month_entry.delete(0, 'end')
                    elif Year.isnumeric() == False or Year == "" or len(Year) >= 5:
                        messagebox.showerror("Error", "Please Enter Valid Year")
                        year_entry.delete(0, 'end')
                    elif Line_1 == "":
                        messagebox.showerror("Error", "Please Fill Address Line 1")
                    elif Line_2 == "":
                        messagebox.showerror("Error", "Please Fill Address Line 2")
                    elif Adhar.isnumeric() == False or Adhar == "" or len(Adhar) != 12:
                        messagebox.showerror("Error", "Please Enter Valid Adhar")
                        adhar_entry.delete(0, 'end')
                    else:

                        try:
                            # print(Name)
                            # print(Age)
                            # print(Gender)
                            # print(Day)
                            # print(Month)
                            # print(Year)
                            # print(Line_1)
                            # print(Line_2)
                            # print(Adhar)                      
                                           

                            try:
                                db = sqlite3.connect("second_child.db")
                                cr = db.cursor()
                                cr.execute("create table if not exists registration (name text, age text, gender text, day text, month text, year text, address_line_1 text, address_line_2 text, adhar text, mobile text)")
                                
                                if Mobile == "":
                                    cr.execute("insert into registration (name, age, gender, day, month, year, address_line_1, address_line_2, adhar, mobile) values(?,?,?,?,?,?,?,?,?,?)",(Name, Age, Gender, Day, Month, Year, Line_1, Line_2, Adhar, None))
                                    messagebox.showinfo("Notification", "Data has been saved!")
                                    db.commit()
                                    db.close()
                                else:
                                    if Mobile.isnumeric() == False or len(Mobile) != 10:
                                        messagebox.showerror("Error", "Please Enter Valid Mobile No.")
                                        mobile_entry.delete(0, 'end')
                                    else:
                                        cr.execute("insert into registration (name, age, gender, day, month, year, address_line_1, address_line_2, adhar, mobile) values('"+Name+"', '"+Age+"', '"+Gender+"', '"+Day+"', '"+Month+"', '"+Year+"', '"+Line_1+"', '"+Line_2+"',  '"+Adhar+"', '"+Mobile+"')")
                                        messagebox.showinfo("Notification", "Data has been saved!")
                                    db.commit()
                                    db.close()
                            except:
                                pass
                        except:
                            pass

                        # messagebox.showinfo("Information","Record Has Been Succesfully Saved!")
                        add_information()


                # Resister button
                resister_button = tk.Button(add_information_frame, text="Resister", font=("Times New Roman",20), width=50, bg="purple", fg="white", command=get_all_registration_info)
                resister_button.place(x=400, y=580)

                
                # # select image button
                # def select_image():
                #     global image_path
                #     try:
                #         image_path = filedialog.askopenfilename(initialdir='/', title="Select Image", filetypes=[("png files", ".png"), ("jpg files", ".jpg"), ("jpeg files", ".jpeg")])
                #         image = Image.open(image_path)

                #         resized_image = image.resize((200, 250))
                #         image2 = ImageTk.PhotoImage(resized_image)

                #         label = tk.Label(add_information_frame, image=image2)
                #         label.image = image2
                #         label.place(x=1250, y=500)
                #         return image_path
                #     except:
                #         pass

                # select_image_button = tk.Button(add_information_frame, text="Add Image", width=17, font=("Times New Roman", 20), command=select_image)
                # select_image_button.place(x=1225, y=775)

                # # Dummy image
                # image = Image.open("old_human_dummy2.png")

                # resized_image = image.resize((200, 250))
                # image2 = ImageTk.PhotoImage(resized_image)

                # label = tk.Label(add_information_frame, image=image2)
                # label.image = image2
                # label.place(x=1250, y=500)

            def view_information():
                view_information_frame = tk.Frame(win, width=WIDTH, height=HEIGHT)
                view_information_frame.place(x=0, y=0)

                # search bar
                search_bar = tk.Entry(view_information_frame, width=30, font=("Times New Roman", 20))
                search_bar.place(x=625, y=20)

                # search button
                search_button = tk.Button(view_information_frame, text="Search", font=("Times New Roman", 18), width=15, bg="#3377ff", fg="white")
                search_button.place(x=1050, y=20)


                def fetch_data():
                    # Connect to the SQLite database
                    conn = sqlite3.connect('second_child.db')
                    cursor = conn.cursor()

                    # Fetch all data from the 'students' table
                    cursor.execute('SELECT name, age, gender, address_line_1, address_line_2,adhar, mobile FROM registration')
                    data = cursor.fetchall()

                    # Close the connection
                    conn.close()

                    return data

                columns = ('Name', 'Age', 'Gender', 'Address_line_1', 'Address_line_2', 'Adhar', 'Mobile')
                tree = ttk.Treeview(view_information_frame, columns=columns, show='headings')

                # Configure column headings
                for col in columns:
                    tree.heading(col, text=col)
                    tree.column(col, anchor='center')

                # Populate the Treeview with data
                data = fetch_data()
                for row in data:
                    tree.insert('', 'end', values=row)

                # Add a vertical scrollbar to the Treeview
                scrollbar = ttk.Scrollbar(view_information_frame, orient='vertical', command=tree.yview)
                tree.configure(yscroll=scrollbar.set)

                # Pack the Treeview and Scrollbar
                tree.place(x=0, y=100, width=1500, height=400)
                scrollbar.place(x=1500, y=100, height=400)



            def add_healthcare_information():
                healthcare_frame = tk.Frame(win, width=WIDTH, height=HEIGHT)

                # heading
                name_label = tk.Label(healthcare_frame, text="HealthCare Information", font=("Times New Roman", 50), fg="purple")
                name_label.place(x=425, y=30)

                # name of patient label
                name_of_patient_label = tk.Label(healthcare_frame, text="Name Of Patient", font=("Times New Roman", 20))
                name_of_patient_label.place(x=50, y=130)

                # name of patient entry
                name_of_patient_entry = tk.Entry(healthcare_frame, font=("Times New Roman", 20), width=36)
                name_of_patient_entry.place(x=250, y=130)


                # name of Doctor label
                name_of_doctor_label = tk.Label(healthcare_frame, text="Name Of Doctor", font=("Times New Roman", 20))
                name_of_doctor_label.place(x=50, y=230)


                # name of doctor entry
                name_of_doctor_entry = tk.Entry(healthcare_frame, font=("Times New Roman", 20), width=36)
                name_of_doctor_entry.place(x=250, y=230)


                # type of disease label
                type_of_disease_label = tk.Label(healthcare_frame, text="Name Of Disease", font=("Times New Roman", 20))
                type_of_disease_label.place(x=50, y=330)                              
                
                # type of desease entry
                type_of_disease_entry = tk.Entry(healthcare_frame, font=("Times New Roman", 20), width=36)
                type_of_disease_entry.place(x=250, y=330)


                # Gender label
                gender_label = tk.Label(healthcare_frame, text="Gender", font=("Times New Roman", 20))
                gender_label.place(x=50, y=430)


                gender = StringVar()
                gender.set("Male")

                # Gender Male
                gender_male = tk.Radiobutton(healthcare_frame, text="Male", value="Male", variable=gender, font=("Times New Roman", 18))
                gender_male.place(x=250, y=430)

                # Gender Female
                gender_female = tk.Radiobutton(healthcare_frame, text="Female", value="Female", variable=gender, font=("Times New Roman", 18))
                gender_female.place(x=450, y=430)

                # Gender Other
                gender_other = tk.Radiobutton(healthcare_frame, text="Other", value="Other", variable=gender, font=("Times New Roman", 18))
                gender_other.place(x=670, y=430)


                # Checkup Date label
                date_label = tk.Label(healthcare_frame, text="Checkup Date", font=("Times New Roman", 20))
                date_label.place(x=50, y=530)


                # day label
                day_label = tk.Label(healthcare_frame, text="Day", font=("Times New Roman", 20))
                day_label.place(x=50, y=580)

                # day entry
                day_entry = tk.Entry(healthcare_frame, font=("Times New Roman", 20), width=8)
                day_entry.place(x=125, y=580)

                # month label
                month_label = tk.Label(healthcare_frame, text="Month", font=("Times New Roman", 20))
                month_label.place(x=300, y=580)


                # month entry
                month_entry = tk.Entry(healthcare_frame, font=("Times New Roman", 20), width=8)
                month_entry.place(x=400, y=580)


                # year label
                year_label = tk.Label(healthcare_frame, text="Year", font=("Times New Roman", 20))
                year_label.place(x=550, y=580)


                # year entry
                year_entry = tk.Entry(healthcare_frame, font=("Times New Roman", 20), width=8)
                year_entry.place(x=635, y=580)

                # Doctor Prescription label
                doctor_prescription_label = tk.Label(healthcare_frame, text="Doctor Prescription", font=("Times New Roman", 20))
                doctor_prescription_label.place(x=875, y=130)

                # doctor prescription on Text
                doctor_prescription = tk.Text(healthcare_frame, width=40, height=15, wrap="word", font=("Times New Roman", 20))
                doctor_prescription.place(x=875, y=170)

                def check_info1(val):
                    for i in range(len(val)):
                        if name_of_patient_entry.get()[i].isnumeric() == True:
                            return True
                        
                def check_info2(val):
                    for i in range(len(val)):
                        if name_of_doctor_entry.get()[i].isnumeric() == True:
                            return True
                        

                def check_info3(val):
                    for i in range(len(val)):
                        if type_of_disease_entry.get()[i].isnumeric() == True:
                            return True

                def get_all_healthcare_info():
                    # print(doctor_prescription.get("1.0","end-1c"))
                    if name_of_patient_entry.get() == "" or name_of_patient_entry.get().isnumeric() == True or check_info1(name_of_patient_entry.get()) == True:
                        messagebox.showerror("Error", "Please Enter Valid Patient Name")
                        name_of_patient_entry.delete(0, 'end')

                    elif name_of_doctor_entry.get() == "" or name_of_doctor_entry.get().isnumeric() == True or check_info2(name_of_doctor_entry.get()) == True:
                        messagebox.showerror("Error", "Please Enter Valid Doctor Name")
                        name_of_doctor_entry.delete(0, 'end')
                        
                    elif type_of_disease_entry.get() == "" or type_of_disease_entry.get().isnumeric() == True or check_info3(type_of_disease_entry.get()) == True:
                        messagebox.showerror("Error", "Please Enter Valid Name Of Disease")
                        type_of_disease_entry.delete(0, 'end')

                    elif day_entry.get() == "" or day_entry.get().isnumeric() == False or int(day_entry.get()) >= 32:
                        messagebox.showerror("Error", "Please Enter Valid Day")
                        day_entry.delete(0, 'end')

                    elif month_entry.get() == "" or month_entry.get().isnumeric() == False or int(day_entry.get()) >= 13:
                        messagebox.showerror("Error", "Please Enter Valid Month")
                        month_entry.delete(0, 'end')
                        
                    elif year_entry.get() == "" or year_entry.get().isnumeric() == False or len(year_entry.get()) >= 5:
                        messagebox.showerror("Error", "Please Enter Valid Year")
                        year_entry.delete(0, 'end')
                    else:
                        # print(name_of_patient_entry.get())
                        # print(name_of_doctor_entry.get())
                        # print(type_of_disease_entry.get())
                        # print(day_entry.get())
                        # print(month_entry.get())
                        # print(year_entry.get())
                        Patient_name = name_of_patient_entry.get()
                        Doctor_name = name_of_doctor_entry.get()
                        Disease = type_of_disease_entry.get()
                        Gender = gender.get()
                        Day = day_entry.get()
                        Month = month_entry.get()
                        Year = year_entry.get()



                        try:
                            db = sqlite3.connect("second_child.db")
                            cr = db.cursor()
                            cr.execute("create table if not exists healthcare (name text, doctor text, disease text, gender text, day text, month text, year text, prescription text)")
                            Prescription = doctor_prescription.get("1.0", tk.END)
                            if Prescription == "":
                                cr.execute("insert into healthcare (name, doctor, disease, gender, day, month, year, prescription) values(?,?,?,?,?,?,?,?)",(Patient_name, Doctor_name, Disease, Gender, Day, Month, Year, None))
                                messagebox.showinfo("Notification", "Data has been saved!")
                                db.commit()
                                db.close()
                            else:
                                cr.execute("insert into healthcare (name, doctor, disease, gender, day, month, year, prescription) values(?,?,?,?,?,?,?,?)",(Patient_name, Doctor_name, Disease, Gender, Day, Month, Year, Prescription))
                                messagebox.showinfo("Notification", "Data has been saved!")
                                db.commit()
                                db.close()
                        except:
                                pass
                        add_healthcare_information()

                
                # Save healthcare information
                healthcare_info = tk.Button(healthcare_frame, text="Save HealthCare Information", font=("Times New Roman", 20), width=50, bg="purple", fg="white", command=get_all_healthcare_info)
                healthcare_info.place(x=400, y=675)


                healthcare_frame.place(x=0, y=0)

            def add_new_donar():
                add_new_donar_frame = tk.Frame(win, width=WIDTH, height=HEIGHT)

                # new donar heading
                name_label = tk.Label(add_new_donar_frame, text="New Donar", font=("Times New Roman", 50), fg="purple")
                name_label.place(x=575, y=30)

                # name label
                name_label = tk.Label(add_new_donar_frame, text="Name", font=("Times New Roman", 20))
                name_label.place(x=50, y=130)

                # name entry
                name_entry = tk.Entry(add_new_donar_frame, font=("Times New Roman", 20), width=36)
                name_entry.place(x=150, y=130)
                

                # mobile no label
                mobile_no_label = tk.Label(add_new_donar_frame, text="Mobile", font=("Times New Roman", 20))
                mobile_no_label.place(x=50, y=230)

                # mobile no entry
                mobile_no_entry = tk.Entry(add_new_donar_frame, font=("Times New Roman", 20), width=36)
                mobile_no_entry.place(x=150, y=230)

                # age label
                age_label = tk.Label(add_new_donar_frame, text="Age", font=("Times New Roman", 20))
                age_label.place(x=50, y=330)


                # age entry
                age_entry = tk.Entry(add_new_donar_frame, font=("Times New Roman", 20), width=36)
                age_entry.place(x=150, y=330)

                # gender label
                age_label = tk.Label(add_new_donar_frame, text="Gender", font=("Times New Roman", 20))
                age_label.place(x=50, y=430)


                Gender = StringVar()
                Gender.set("Male")

                # Gender Male
                gender_male = tk.Radiobutton(add_new_donar_frame, text="Male", font=("Times New Roman", 18), value="Male", variable=Gender)
                gender_male.place(x=225, y=430)

                # Gender Female
                gender_female = tk.Radiobutton(add_new_donar_frame, text="Female", font=("Times New Roman", 18), value="Female", variable=Gender)
                gender_female.place(x=370, y=430)

                # Gender Other
                gender_other = tk.Radiobutton(add_new_donar_frame, text="Other", font=("Times New Roman", 18), value="Other", variable=Gender)
                gender_other.place(x=525, y=430)


                # adhar no label
                adhar_label = tk.Label(add_new_donar_frame, text="Aadhar", font=("Times New Roman", 20))
                adhar_label.place(x=50, y=530)

                # adhar no entry
                adhar_entry = tk.Entry(add_new_donar_frame, font=("Times New Roman", 20), width=36)
                adhar_entry.place(x=150, y=530)

                # address label 1 label
                address_label_1_label = tk.Label(add_new_donar_frame, text="Address Line 1", font=("Times New Roman", 20))
                address_label_1_label.place(x=775, y=130)

                # address label 1 entry
                address_label_1_entry = tk.Entry(add_new_donar_frame, font=("Times New Roman", 20), width=36)
                address_label_1_entry.place(x=975, y=130)

                # address entry 2 label
                address_label_2 = tk.Label(add_new_donar_frame, text="Address Line 2", font=("Times New Roman", 20))
                address_label_2.place(x=775, y=230)

                # address entry 2 entry
                address_label_2_entry = tk.Entry(add_new_donar_frame, font=("Times New Roman", 20), width=36)
                address_label_2_entry.place(x=975, y=230)

                # type of donation label
                type_of_donation_label = tk.Label(add_new_donar_frame, text="Donation", font=("Times New Roman", 20))
                type_of_donation_label.place(x=775, y=330)

                # type of donation entry
                type_of_donation_entry = tk.Entry(add_new_donar_frame, font=("Times New Roman", 20), width=36)
                type_of_donation_entry.place(x=975, y=330)

                # Donation Date label
                date_label = tk.Label(add_new_donar_frame, text="Donation Date", font=("Times New Roman", 20))
                date_label.place(x=775, y=430)


                # day label
                day_label = tk.Label(add_new_donar_frame, text="Day", font=("Times New Roman", 20))
                day_label.place(x=850, y=475)

                # day entry
                day_entry = tk.Entry(add_new_donar_frame, font=("Times New Roman", 20), width=8)
                day_entry.place(x=920, y=475)

                # month label
                month_label = tk.Label(add_new_donar_frame, text="Month", font=("Times New Roman", 20))
                month_label.place(x=1050, y=475)


                # month entry
                month_entry = tk.Entry(add_new_donar_frame, font=("Times New Roman", 20), width=8)
                month_entry.place(x=1150, y=475)


                # # year label
                year_label = tk.Label(add_new_donar_frame, text="Year", font=("Times New Roman", 20))
                year_label.place(x=1280, y=475)


                # year entry
                year_entry = tk.Entry(add_new_donar_frame, font=("Times New Roman", 20), width=8)
                year_entry.place(x=1355, y=475)


                def check_info1(val):
                    for i in range(len(val)):
                        if name_entry.get()[i].isnumeric() == True:
                            return True

                def get_all_donar_info():
                    
                    # donar validation

                    if name_entry.get().isnumeric() == True or name_entry.get() == "" or check_info1(name_entry.get()) == True:
                        messagebox.showerror("Error", "Please Enter Valid Name")
                        name_entry.delete(0, 'end')

                    elif mobile_no_entry.get().isnumeric() == False or mobile_no_entry.get() == "" or len(mobile_no_entry.get()) != 10:
                        messagebox.showerror("Error", "Please Enter Valid Mobile No.")
                        mobile_no_entry.delete(0, 'end')

                    elif age_entry.get().isnumeric() == False or age_entry.get() == "":
                        messagebox.showerror("Error", "Please Enter Valid Age")
                        age_entry.delete(0, 'end')

                    elif adhar_entry.get().isnumeric() == False or adhar_entry.get() == "" or len(adhar_entry.get()) != 12:
                        messagebox.showerror("Error", "Please Enter Valid Adhar")
                        adhar_entry.delete(0, 'end')

                    elif address_label_1_entry.get() == "":
                        messagebox.showerror("Error", "Please Fill Address Line 1")

                    elif address_label_2_entry.get() == "":
                        messagebox.showerror("Error", "Please Fill Address Line 2")

                    elif type_of_donation_entry.get() == "":
                        messagebox.showerror("Error", "Please Enter Valid Donation")

                    elif day_entry.get().isnumeric() == False or day_entry.get() == "" or int(day_entry.get()) > 31:
                        messagebox.showerror("Erro", "Please Enter Valid Day")
                        day_entry.delete(0, 'end')

                    elif month_entry.get().isnumeric == False or month_entry.get() == "" or int(month_entry.get()) > 12:
                        messagebox.showerror("Error", "Please Enter Valid Month")
                        month_entry.delete(0, 'end')

                    elif year_entry.get().isnumeric == False or year_entry.get() == "" or len(year_entry.get()) >= 5:
                        messagebox.showerror("Error", "Please Enter Valid Year")
                        year_entry.delete(0, 'end')

                    else:
                        # print(name_entry.get())
                        # print(mobile_no_entry.get())
                        # print(age_entry.get())
                        # print(Gender.get())
                        # print(adhar_entry.get())
                        # print(address_label_1_entry.get())
                        # print(address_label_2_entry.get())
                        # print(type_of_donation_entry.get())
                        # print(day_entry.get())
                        # print(month_entry.get())
                        # print(year_entry.get())

                        # Name = name_entry.get()

                        # try:
                        #     db = sqlite3.connect("second_child.db")
                        #     cr = db.cursor()
                        #     cr.execute("create table if not exists donar(name text, mobile text, age text, gender text, adhar text, address_line_1 text, address_line_2 text, donation text, day text, month text, year text)")
                        #     cr.execute("insert into donar (name, mobile, age, gender, adhar, address_line_1, address_line_2, donation, day, month, year) values(?,?,?,?,?,?,?,?,?,?,?)", ())
                        #     db.commit()
                        #     db.close()
                        #     messagebox.showinfo("Notification", "Data has been saved!")
                        # except:
                        #     pass
                        add_new_donar()


                # register donar button
                register_donar_button = tk.Button(add_new_donar_frame, text="Register Donar", font=("Times New Roman", 20), bg="purple", fg="white", width=50, command=get_all_donar_info)
                register_donar_button.place(x=390, y=650)

                add_new_donar_frame.place(x=0, y=0)

            if username_entry.get() == "Admin" and password_entry.get() == "***":
                frame1.destroy() 
                after_login_frame = tk.Frame(win, width=WIDTH, height=HEIGHT)

                
                path2 = 'second_childhood3.jpg'

                # Create an object of tkinter ImageTk
                image1 = Image.open(path2)
                resized_image2 = image1.resize((WIDTH, HEIGHT))
                img = ImageTk.PhotoImage(resized_image2)

                # Create a Label Widget to display the text or Image
                label1 = tk.Label(after_login_frame, image = img)
                label1.image = img
                label1.place(x=0, y=0)

                path = 'shantai.png'
                image2 = Image.open(path)
                resized_image2 = image2.resize((200, 200))

                image3 = ImageTk.PhotoImage(resized_image2)
                label2 = tk.Label(after_login_frame, image=image3)
                label2.image = image3
                label2.place(x=100, y=100)

                my_menu = tk.Menu(win, font=("Ariel", 20))
                win.config(menu=my_menu)

                edit_menu = tk.Menu(my_menu)
                my_menu.add_cascade(label='  Home  ', menu=edit_menu)
                edit_menu.add_command(label='Home', font=("Ariel", 16), command=after_login)

                file_menu = tk.Menu(my_menu)
                my_menu.add_cascade(label='  Residence  ', menu=file_menu)
                file_menu.add_command(label='Add New Residence', font=("Ariel", 16), command=add_information)
                file_menu.add_separator()
                file_menu.add_command(label='View Information', font=("Ariel", 16), command=view_information)
                
                service_menu = tk.Menu(my_menu)
                my_menu.add_cascade(label="HealthCare", menu=service_menu)
                service_menu.add_command(label='Add HealthCare Information', font=("Ariel", 16), command=add_healthcare_information)
                service_menu.add_separator()
                service_menu.add_command(label='View HealthCare Information', font=("Ariel", 16), command=None)


                information_menu = tk.Menu(my_menu)
                my_menu.add_cascade(label='  Donations  ', menu=information_menu)
                information_menu.add_command(label='Add New Donar', font=("Ariel", 16), command=add_new_donar)
                information_menu.add_separator()
                information_menu.add_command(label='View All Donations', font=("Ariel", 16), command=None)
                

                after_login_frame.place(x=0,y=0)
                
            else:    
                messagebox.showerror("Error", "Please Enter Correct Credentials!")
        # Submit button
        submit_button = tk.Button(frame1, text="Submit", font=("Ariel", 18), command=after_login)
        submit_button.place(x=200, y=275)

        # Account Form
        def create_an_account():
            frame1.destroy()
            name_frame = tk.Frame(win, width=600, height=750, bg='#D6D7E8')

            # first name label
            first_name_label = tk.Label(name_frame, text="First Name", font=("Ariel", 18), bg='#D6D7E8')
            first_name_label.place(x=75,y=40)

            # first name text input
            first_name_entry = tk.Entry(name_frame, width=34, font=("Ariel", 18))
            first_name_entry.place(x=75, y=80)
            
            # last name label
            last_name_label = tk.Label(name_frame, text="Last Name", font=("Ariel", 18), bg='#D6D7E8')
            last_name_label.place(x=75,y=180)

            # last name text input
            last_name_entry = tk.Entry(name_frame, width=34, font=("Ariel", 18))
            last_name_entry.place(x=75, y=220)


            # username label
            user_name_label = tk.Label(name_frame, text="User Name", font=("Ariel", 18), bg='#D6D7E8')
            user_name_label.place(x=75,y=320)
            
            # user name text input
            user_name_entry = tk.Entry(name_frame, width=34, font=("Ariel", 18))
            user_name_entry.place(x=75, y=360)


            # password lable
            password_label = tk.Label(name_frame, text="Password", font=("Ariel", 18), bg='#D6D7E8')
            password_label.place(x=75, y=460)


            # Password text input
            password_entry = tk.Entry(name_frame, width=34, font=("Ariel", 18))
            password_entry.place(x=75, y=500)


            # Submit Button
            submit_button = tk.Button(name_frame, text="Submit", font=("Ariel", 18), command=first_page)
            submit_button.place(x=250, y=600)

            name_frame.place(relx=0.5, rely=0.5, anchor='center')

        # Create an account button
        create_accout_button = tk.Button(frame1, text="Create an Account", width=31, font=("Ariel", 18), command=create_an_account)
        create_accout_button.place(x=25, y=350)


    inner_first_page()
    
    first_frame.place(x=0,y=0)

first_page()

win.mainloop()