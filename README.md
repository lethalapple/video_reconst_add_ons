# video_reconst_add_ons

High Speed and High Dynamic Range Video with an Event Camera https://github.com/uzh-rpg/rpg_e2vid

Extract events from inivation data file
python extract_inivation_events.py

Insert resolution into data file
python edit_events_file.py

Run the video reconstruction
python run_reconstruction.py -c pretrained/E2VID_lightweight.pth.tar -i data/MyFile.zip --auto_hdr --display --show_events --output_folder out_vid

Create the video
python create_vid.py
