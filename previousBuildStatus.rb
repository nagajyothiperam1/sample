# UpdateBuildRecordStatus.rb
#
  
# Open DashboardDB and update status of previous build record to the provided target status, all arguments are required.
# Mostly changes the build record from STARTED to ABORTED
#
# 
# 2018-	jyothi
#
# Options:
#  -f, --filename=<s>       Database configuration file, required
#  -b, --branch=<s>         Branch, required
#  -r, --from=<s>           Current build status
#  -t, --to=<s>             Build status to be changed to
#  -s, --status_desc=<s>	  status description
#  -h, --help               Show this message
#

# required gems
require 'trollop'    # for parsing arguments
require 'nokogiri' # for parsing xml files
require 'mysql2'

begin
  
  opts = Trollop::options do
	opt :filename, "Database configuration file, required", :type => String
	opt :branch, "Branch, required", :type => String
	opt :from, "Current build status, required", :type => String
    opt :to, "Build status to be changed to, required", :type => String
	opt :status_desc, "status description, optional", :type => String
  end
   
 
  # Verify all required args have been supplied
  if !(opts[:filename_given] && opts[:branch_given] && opts[:build_number] && opts[:from_given] && opts[:to_given])
	unless opts[:filename_given]
	  puts "argument- configuration filename missing"
	end
	unless opts[:branch_given]
		puts "argument- branch missing"
	end
	unless opts[:build_number]
		puts "argument- from build number missing"
	end
	unless opts[:from_given]
		puts "argument- from status missing"
	end
	unless opts[:to_given]
		puts "argument- to status missing"
	end
	abort "\nERROR. Aborting script. \nMissing argument(s)"
  end
  
  # DEBUG
  puts "db config filename: " + opts[:filename]
  
  # Test if files exist and are readable
  abort "Error: Supplied config file (" + opts[:filename] + ") not readable" unless File.readable?(opts[:filename])
  # if exist and readable opts[:filename]
  
  # get database configuration from config file
  
  # open and parse config file to get: hostname, username, password, dbname
  config = Nokogiri::XML(File.open(opts[:filename]))
  
  database = config.at_xpath('//database')
  host = database.at_xpath('//host').content
  username = database.at_xpath('//username').content
  password = database.at_xpath('//password').content
  databasename = database.at_xpath('//databasename').content
  
  dashboardDB = Mysql2::Client.new(:host => host, :username => username,  :password => password, :databasename => databasename)
  sql_query = "use " + databasename 
  dashboardDB.query (sql_query)
  
  #previous build number
  build=opts[:build_number].to_i
  prev_build=build-1
  opts[:build_number]=prev_build.to_s
  
  #puts "create query"
  sql_query = "UPDATE t_buildstatus set c_status='#{opts[:to]}', c_status_desc='#{opts[:status_desc]}' where c_branch='#{opts[:branch]}' and c_build='#{opts[:build_number]}' and c_status='#{opts[:from]}' "
  puts sql_query
  
  rs_update = dashboardDB.query(sql_query)
  puts "\n\n"

rescue Mysql2::Error => e
  puts "SQL error caught"
  puts e.errno
  puts e.error
	
ensure
  dashboardDB.close if dashboardDB
  puts "UpdateBuildRecordStatus.rb completed."

end