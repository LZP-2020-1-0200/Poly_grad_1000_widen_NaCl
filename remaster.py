import analyzer as h
import cnst as c

h.prepare_clean_output_folder('data_out')
h.open_ZipSession('data_in/14.02.23.zip')
h.open_SQLiteSession('14.02.23.sqlite3')
h.find_session_json('session.json')
h.find_timestamps_files('spectra_ts_14-15_feb2023.txt',
                        'clickerino_ts_14-15_feb2023.txt')
h.fill_file_table(('14.02.23/spectra_ts_14-15_feb2023.txt',
                  '14.02.23/session.json',
                   '14.02.23/pieraksti.txt',
                   'xyz',
                   'xyz'
                   ))
h.fill_spots_table()
h.fill_jpg_file_table()
h.update_spectra_timestamps_in_file_table()


# h.print_reference_file_names()

h.fill_reference_sets((
    ('14.02.23/refs/white01.asc',
     '14.02.23/refs/darkForWhite01.asc',
     '14.02.23/refs/dark01.asc',
     c.UNPOL),
    ('14.02.23/refs/white02.asc',
     '14.02.23/refs/darkForWhite02.asc',
     '14.02.23/refs/dark02.asc',
     c.P_POL),
    ('14.02.23/refs/white03.asc',
     '14.02.23/refs/darkForWhite03.asc',
     '14.02.23/refs/dark03.asc',
     c.S_POL),
    ('14.02.23/refs/white04.asc',
     '14.02.23/refs/darkForWhite04.asc',
     '14.02.23/refs/dark04.asc',
     c.UNPOL),
    ('14.02.23/refs/white05.asc',
     '14.02.23/refs/darkForWhite05.asc',
     '14.02.23/refs/dark05.asc',
     c.S_POL),
    ('14.02.23/refs/white06.asc',
     '14.02.23/refs/darkForWhite06.asc',
     '14.02.23/refs/dark06.asc',
     c.P_POL)
))

h.plot_reference_sets()

h.config_series()
h.assign_img_to_spectra()

h.plotspectra()

h.combine_pdf_files()