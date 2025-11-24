# Testing Guide - Medical History Features

## Quick Start

1. **Start the application:**
```bash
cd doctor-appointment-system-main
python app.py
```

2. **Open browser:** http://localhost:5000

## Test Accounts

| Role | Email | Password |
|------|-------|----------|
| Patient | patient@test.com | patient123 |
| Doctor | doctor@test.com | doctor123 |
| Hospital Admin | admin@test.com | admin123 |

## Testing Flow

### Step 1: Book an Appointment (as Patient)
1. Login as patient: `patient@test.com` / `patient123`
2. Click "Hospitals" or browse available hospitals
3. Select "Test General Hospital"
4. Click "Book Appointment" for Dr. John Smith
5. Fill in:
   - Date: Tomorrow's date
   - Time: Any time
   - Symptoms: "Fever and headache for 3 days"
6. Submit the appointment

### Step 2: Approve Appointment (as Doctor)
1. Logout and login as doctor: `doctor@test.com` / `doctor123`
2. You'll see the pending appointment
3. Click "Accept" to approve the appointment

### Step 3: Add Medical Records (as Doctor)
1. Go to "Today's Appointments" (if appointment is today) or wait
2. Click "Add Medical Records" button
3. Fill in the medical information:
   - **Diagnosis:** "Viral fever with mild dehydration"
   - **Prescription:**
     ```
     1. Paracetamol 500mg - 3 times daily for 5 days
     2. ORS Solution - 2 sachets daily
     3. Rest and plenty of fluids
     ```
   - **Treatment Plan:** "Rest for 3 days, avoid cold foods, drink warm water"
   - **Test Results:** "Temperature: 101°F, BP: 120/80"
   - **Follow-up Date:** Select a date 1 week from now
   - **Doctor Notes:** "Patient seems stressed, recommend stress management"
4. Check "Mark this appointment as completed"
5. Click "Save Medical Records"

### Step 4: View Medical History (as Patient)
1. Logout and login as patient: `patient@test.com` / `patient123`
2. Click "View Medical History" button on dashboard
3. You'll see the complete medical record including:
   - Diagnosis
   - Prescription
   - Treatment plan
   - Test results
   - Follow-up recommendation
4. Click "View Full Details" to see more information
5. If follow-up is recommended, click "Book Follow-up Appointment"

### Step 5: Check Dashboard Features
**Patient Dashboard:**
- See "Upcoming Appointments" count
- See "Completed Appointments" count
- View past appointments in "Past Appointments" section
- Click any appointment to view full details

**Doctor Dashboard:**
- Pending appointments with Accept/Reject buttons
- Today's appointments with "Add Medical Records" button
- Upcoming appointments list
- Completed appointments with "View Records" button

## Features to Test

### ✅ Patient Features
- [ ] Book new appointment
- [ ] View upcoming appointments
- [ ] View past appointments
- [ ] Access medical history page
- [ ] View detailed appointment information
- [ ] See diagnosis and prescriptions
- [ ] Check follow-up recommendations
- [ ] Book follow-up appointments
- [ ] Cancel pending appointments

### ✅ Doctor Features
- [ ] View pending appointments
- [ ] Approve/reject appointments
- [ ] Add medical records
- [ ] Update existing medical records
- [ ] Add diagnosis
- [ ] Write prescriptions
- [ ] Create treatment plans
- [ ] Record test results
- [ ] Set follow-up dates
- [ ] Add private doctor notes
- [ ] Mark appointments as completed
- [ ] View completed appointment records

## Expected Results

1. **Medical History Page** should show:
   - All completed appointments in chronological order
   - Complete medical information for each visit
   - Color-coded sections for easy reading
   - Follow-up recommendations highlighted

2. **Appointment Details** should display:
   - Patient/Doctor information
   - Hospital details
   - Symptoms reported
   - Complete medical records (if completed)
   - Status badges with appropriate colors

3. **Doctor's Medical Records Form** should:
   - Pre-fill existing data when editing
   - Save all fields correctly
   - Update appointment status to "completed"
   - Set completion timestamp

## Troubleshooting

**Issue:** No test data showing
- **Solution:** Run `python -c "from app import init_db; init_db()"`

**Issue:** Database errors
- **Solution:** Run `python migrate_db.py` to reset database

**Issue:** Can't see medical records
- **Solution:** Make sure appointment is marked as "completed" by doctor

**Issue:** Follow-up date not showing
- **Solution:** Doctor must set a follow-up date in the medical records form

## Database Viewing

To view database contents anytime:
```bash
python view_data.py
```

This will show all tables and their data in a formatted view.
